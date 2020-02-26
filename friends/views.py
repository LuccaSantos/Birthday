from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import FriendForm, EmailForm
from .models import Friend
from django.contrib import messages
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail, BadHeaderError


@login_required
def friendList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    date_today = date.today()

    friends = Friend.objects.filter(birthday=date_today, user=request.user).count()
    if friends >= 1:
        send_mail('BIRTHDAY', 'Today is a birthday of a friend', 'teste@gmail.com', ['admin@example.com'])

    if search:
        friends = Friend.objects.filter(
            name__icontains=search, user=request.user)

    elif filter == 'today':
        friends = Friend.objects.filter(
            birthday=date_today, user=request.user)

    elif filter == 'this-month':
        max_date = (date_today + relativedelta(months=1))
        friends = Friend.objects.filter(birthday__range=(
            date_today, max_date), user=request.user)

    elif filter == 'next-month':
        min_date = date_today + relativedelta(months=1)
        max_date = date_today + relativedelta(months=2)
        friends = Friend.objects.filter(birthday__range=(
            min_date, max_date), user=request.user)

    else:
        friends_list = Friend.objects.all().filter(user=request.user)
        paginator = Paginator(friends_list, 10)
        page = request.GET.get('page')
        friends = paginator.get_page(page)
        # friends = Friend.objects.all().filter(user=request.user)

    return render(request, 'friends/friend-list.html', {'friends': friends})


@login_required
def friendView(request, id):
    friend = get_object_or_404(Friend, pk=id)
    return render(request, 'friends/friend-view.html', {'friend': friend})


@login_required
def createFriend(request):

    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.user = request.user
            friend.save()
            messages.info(request, 'Friend Created')

            return redirect('/')
    else:
        form = FriendForm()
        return render(request, 'friends/create-friend.html', {'form': form})


@login_required
def editFriend(request, id):
    friend = get_object_or_404(Friend, pk=id)
    form = FriendForm(instance=friend)

    if request.method == 'POST':
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            friend.save()
            messages.info(request, 'Updated Friend')
            return redirect('/')
        else:
            return render(request, 'friends/edit-friend.html', {'form': form, 'friend': friend})

    else:
        return render(request, 'friends/edit-friend.html', {'form': form, 'friend': friend})


@login_required
def deleteFriend(request, id):
    friend = get_object_or_404(Friend, pk=id)
    friend.delete()
    messages.info(request, 'Friend Deleted')
    return redirect('/')