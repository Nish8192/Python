from django.shortcuts import render, HttpResponse, redirect
import random
# from django import forms
# from .forms import PostForm
# Create your views here.

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['MESSAGE'] = ''
        request.session['boss'] = 'display: none'

    if request.session['total_gold'] < 0:
        request.session['MESSAGE'] = 'PIT BOSS ARRIVES AND BREAKS YOUR KNEE CAPS :('
        request.session['boss'] = 'display: block'
    print request.session['total_gold']
    return render(request, 'Play_Game/index.html')

def processDaMoney(request):
    form = request.POST
    print form
    # return redirect('/')
    if request.method == 'POST':
        if form['action'] == 'farm':
            request.session['total_gold'] += random.randrange(10,20)
            print request.session['total_gold']
            return redirect('/')
        elif form['action'] == 'cave':
            request.session['total_gold'] += random.randrange(5,10)
            print request.session['total_gold']
            return redirect('/')
        elif form['action'] == 'house':
            request.session['total_gold'] += random.randrange(2,5)
            print request.session['total_gold']
            return redirect('/')
        elif form['action'] == 'casino':
            request.session['total_gold'] += random.randrange(-50,50)
            print request.session['total_gold']
            return redirect('/')
        elif form['action'] == 'reset':
            request.session.clear()
            return redirect('/')
    else:
        return redirect('/')
