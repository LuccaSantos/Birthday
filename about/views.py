from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import EmailForm


def about(request):
    form = EmailForm()
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    if subject and message and email:
        try:
            send_mail(subject, message, email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return  HttpResponse('lancou a braba fdp.')
    else:
        return render(request, 'about/about.html', {'form':form})


def sucessEmail(request):
    return render(request, 'friends/sucess-email.html')