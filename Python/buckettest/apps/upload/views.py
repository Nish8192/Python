from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import ImgForm
from .models import Images
import boto3
s3 = boto3.resource('s3')


# Create your views here.

def index(request):
    form = ImgForm()
    data = {
    'form' : form,
    'img' : Images.objects.all()
    }
    return render(request, 'upload/index.html', data)

def image(request):
    user_id = request.session.get('active_user_id')
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        print request.FILES['imgfile']
        if form.is_valid():
            update = Images.objects.create(avatar=request.FILES['imgfile'])
    return redirect(reverse('upload:index'))
