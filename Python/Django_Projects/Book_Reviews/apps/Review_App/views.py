from django.shortcuts import render, redirect
from .models import User, Review, Book, Author
import bcrypt
from django.contrib import messages
from datetime import datetime
# Create your views here.

def index(request):
    if 'log_user_id' not in request.session:
        request.session['log_user_id'] = 0
        request.session['log_user_name'] = ''
        request.session['log_user_alias'] = ''
    context = {
    'messages': messages.get_messages(request)
    }
    return render(request, 'Review_App/index.html', context)

def goHome(request):
    context = {
    'recent_reviews': Review.objects.all().order_by('created_at')[0:3]
    }
    return render(request, 'Review_App/Home.html', context)

def add_page(request):
    context = {
    'authors': Author.objects.all()
    }
    return render(request, 'Review_App/Add_Book_and_Review.html', context)

def addBook(request):
    if request.method == 'POST':
        book_title = request.POST['title']
        if request.POST['new_author'] == '':
            book_author = request.POST['author']
        else:
            book_author = Author.objects.create(name = request.POST['new_author'])
        review = request.POST['new_review']
        new_book = Book.objects.create(title = book_title, book_author = book_author)
        Review.objects.create(content = review, stars = request.POST['rating'], user_reviewed = request.session['log_user_id'], book_reviewed = new_book.id)
    return redirect('/home')

def createUser(request):
    if request.method == 'POST':
        context = {
        'recent_reviews': Review.objects.all().order_by('created_at')[0:3]
        }
        flag = True
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        alias = request.POST['alias']
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
                user = User.objects.create(first_name=first_name, last_name=last_name, alias=alias, email=email, password=hashed, birthday=bday)
                request.session['log_user_id'] = user.id
                request.session['log_user_name'] = user.first_name
                request.session['log_user_alias'] = user.alias
                return render(request, 'Review_App/Home.html', context)
        else:
            messages.error(request, 'This email address is already registered, please log in below!')
    return redirect('/')

def logOut(request):
    request.session.clear()
    redirect('/')

def logIn(request):
    if request.method == 'POST':
        context = {
        'recent_reviews': Review.objects.all().order_by('created_at')[0:3]
        }
        email = request.POST['email_address']
        password = str(request.POST['pw'])
        users = User.objects.filter(email=email)
        if not users:
            messages.error(request, 'This user does not exist!')
            return redirect('/')
        for user in users:
            if bcrypt.hashpw(password, str(user.password)) == str(user.password):
                request.session['log_user_id'] = user.id
                request.session['log_user_name'] = user.first_name
                request.session['log_user_alias'] = user.alias
                return render(request, 'Review_App/Home.html', context)
            else:
                messages.error(request, 'Sorry, invalid password')
                return redirect('/')

    return redirect('/')
