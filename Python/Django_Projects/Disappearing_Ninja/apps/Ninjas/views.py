from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'Ninjas/index.html')

def showAll(request):
    return render(request, 'Ninjas/ninjas.html')

def showNinja(request, color='black'):
    color = color
    if(color == 'blue'):
        return render(request, 'Ninjas/blue.html')
    if(color == 'orange'):
        return render(request, 'Ninjas/orange.html')
    if(color == 'red'):
        return render(request, 'Ninjas/red.html')
    if(color == 'purple'):
        return render(request, 'Ninjas/purple.html')
    else:
        return render(request, 'Ninjas/meganfox.html')
