from django.shortcuts import get_object_or_404, redirect, render

from .forms import FriendForm
from .models import Friend


def friendList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    # create the logic of the filter

    if search:
        friends = Friend.objects.filter(name__icontains=search)
    elif filter:
        friends = Friend.objects.filter()
    else:
        friends = Friend.objects.all()
    return render(request, 'friends/friend-list.html', {'friends': friends})


def friendView(request, id):
    friend = get_object_or_404(Friend, pk=id)
    return render(request, 'friends/friend-view.html', {'friend': friend})


def createFriend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.save()
            return redirect('/')
    else:
        form = FriendForm()
        return render(request, 'friends/create-friend.html', {'form': form})


def editFriend(request, id):
    friend = get_object_or_404(Friend, pk=id)
    form = FriendForm(instance=friend)

    if request.method == 'POST':
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            friend.save()
            return redirect('/')
        else:
            return render(request, 'friends/edit-friend.html', {'form': form, 'friend': friend})

    else:
        return render(request, 'friends/edit-friend.html', {'form': form, 'friend': friend})


def deleteFriend(request , id):
    friend = get_object_or_404(Friend, pk=id)
    friend.delete()
    return redirect('/')
