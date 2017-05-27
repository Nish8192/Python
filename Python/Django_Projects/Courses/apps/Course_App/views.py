from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.


def index(request):
    context = {
    'Courses': Courses.objects.all()
    }
    return render(request, 'Course_App/index.html', context)

def addCourse(request):
    if request.method == 'POST':
        Courses.objects.create(name = request.POST['new_course_name'], description = request.POST['new_course_desc'])
    return redirect('/')

def deleteCourse(request, id):
    Courses.objects.get(id=id).delete()
    return redirect('/')
