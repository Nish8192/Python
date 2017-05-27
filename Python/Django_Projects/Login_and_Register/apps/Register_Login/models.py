from __future__ import unicode_literals
import re
from django.db import models
from datetime import date, datetime

# Create your models here.
class UserManager(models.Manager):
    def login(self, email, pw):
        pass

    def oldEnough(self, birthday):
        today = datetime.strptime(str(date.today()), '%Y-%m-%d')
        age = (today - birthday).days
        if age >= 6570:
            return True
        else:
            return False

    def confirmPassword(self, pw, pwc):
        return pw == pwc

    def validPassword(self, pw):
        valid_password_pattern = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        return re.match(valid_password_pattern, pw)

    def validFirst_Name(self, first_name):
        if len(first_name) > 1:
            return True
        else:
            return False

    def validLast_Name(self, last_name):
        if len(last_name) > 1:
            return True
        else:
            return False

    def validateEmail(self, email):
        valid_email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        return valid_email_pattern.match(email)

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
