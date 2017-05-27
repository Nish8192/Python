from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
from datetime import datetime
# Create your views here.

def index(request):
    context = {
    'messages': messages.get_messages(request)
    }
    return render(request, 'Register_Login/index.html', context)

def createUser(request):
    if request.method == 'POST':
        flag = True
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email_address']
        pw = str(request.POST['pw'])
        pwc = str(request.POST['pwc'])

        bday = datetime.strptime(str(request.POST['birthday']), '%Y-%m-%d')
        print bday

        users = User.objects.filter(email=email)
        if not users:
            if not User.objects.validFirst_Name(first_name):
                messages.error(request, 'First Name must be at least two characters')
                flag = False
            if not User.objects.validLast_Name(last_name):
                messages.error(request, 'Last Name must be at least two characters')
                flag = False
            if not User.objects.validateEmail(email):
                messages.error(request, 'Please enter a valid email address')
                flag = False
            if not User.objects.validPassword(pw):
                messages.error(request, 'Please enter a valid password, at least 8 characters long, using letters, numbers, or special characters (@#$%^&+=)')
                flag = False
            if not User.objects.confirmPassword(pw, pwc):
                messages.error(request, 'The entered passwords do not match')
                flag = False
            if not User.objects.oldEnough(bday):
                messages.error(request, 'You are not old enough to create an account with us :(')
                flag = False
            if flag:
                hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
                User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed, birthday=bday)
                return render(request, 'Register_Login/success.html')
        else:
            messages.error(request, 'This email address is already registered, please log in below!')
    return redirect('/')

def logIn(request):
    if request.method == 'POST':
        email = request.POST['email_address']
        password = str(request.POST['pw'])
        users = User.objects.filter(email=email)
        if not users:
            messages.error(request, 'This user does not exist!')
            return redirect('/')
        for user in users:
            if bcrypt.hashpw(password, str(user.password)) == str(user.password):
                return render(request, 'Register_Login/success.html')
            else:
                messages.error(request, 'Sorry, invalid password')
                return redirect('/')

    return redirect('/')
