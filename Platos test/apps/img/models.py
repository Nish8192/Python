from __future__ import unicode_literals

from django.db import models
from ..login_register.models import User

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, related_name="user_image")
    avatar = models.ImageField(upload_to='login_register/avatar/', default='default/default.jpg')
