from __future__ import unicode_literals
from ..Register_Login.models import User
from ..Course_App.models import Courses
from django.db import models

# Create your models here.
class RegistrationManager(models.Manager):
    def isRepeat(self, user_id, course_id):
        check = Registration.objects.filter(user = user_id).filter(courses=course_id)
        if not check:
            return True
        else:
            print 'User is already registered'
            return False



class Registration(models.Model):
    user = models.ForeignKey(User, related_name = 'Users')
    courses = models.ForeignKey(Courses, related_name = 'courseRegister')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegistrationManager()
