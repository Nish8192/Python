from django.shortcuts import render, HttpResponse, redirect
import random, string
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'RandWord/index.html')

def generateRandWord(request):
    if request.method == 'POST':
        request.session['count'] += 1
        request.session['word'] = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in xrange(14)])
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
