from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
    'emails': Email.objects.all(),
    'messages': messages.get_messages(request)
    }
    return render(request, 'Validate_Email/index.html', context)

def checkEmail(request):
    if request.method == "POST":
        if Email.objects.validateEmail(request.POST['address']):
            Email.objects.create(email_address = request.POST['address'])
            messages.success(request, 'Your email address was successfully added!')
        else:
            messages.error(request, 'That is not a valid email address. Please try again :(')
    return redirect('/')

def removeEmail(request, id):
    Email.objects.get(id=id).delete()
    return redirect('/')
