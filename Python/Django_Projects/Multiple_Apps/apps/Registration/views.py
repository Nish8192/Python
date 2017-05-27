from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..Register_Login.models import User
from ..Course_App.models import Courses
from .models import Registration
from django.db.models import Count
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
    'users': User.objects.all(),
    'courses': Courses.objects.all(),
    'registrations': Courses.objects.annotate(num_users=Count('courseRegister')),
    'messages': messages.get_messages(request)
    }
    return render(request, 'Registration/index.html', context)

def register(request):
    if request.method == 'POST':
        if Registration.objects.isRepeat(request.POST['userToRegister'], request.POST['courseToRegister']):
            Registration.objects.create(user_id=request.POST['userToRegister'], courses_id=request.POST['courseToRegister'])
        else:
            messages.error(request, 'Sorry, this user is already registered to this course, please select a different user/course')
    return redirect(reverse('Registration:index'))
