from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class EmailValidator(models.Manager):
    def validateEmail(self, email):
        valid_email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        return valid_email_pattern.match(email)


class Email(models.Model):
    email_address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailValidator()
