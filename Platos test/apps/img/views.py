from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from ..login_register.models import User, UserManager
from models import Image
from forms import ImgForm

# Create your views here.
def index(request):
    # user_id = request.session.get('active_user_id')
    user = User.objects.get(id = request.session.get('active_user_id'))
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            delete = Image.objects.filter(user = user).delete()
            update = Image.objects.filter(user = user).create(avatar=request.FILES['imgfile'], user = user)
            return redirect(reverse('img:index'))
    else:
        form = ImgForm()
    Images = User.objects.all()
    data = {
        'user' : Image.objects.filter(user = user),
        'form' : form
        }
    return render(request, 'img/index.html', data)
