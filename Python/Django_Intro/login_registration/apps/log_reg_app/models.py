from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.validators import RegexValidator
import re
import bcrypt
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import views as auth_views

NAME_REGEX2 = re.compile(r'^([a-zA-Z ]*)$')

class UserManager(models.Manager):
    def validate(self, post_data): 
        errors = []
        if not NAME_REGEX2.match(post_data['first_name']):
            errors.append("Please only use letters in your first name")
        if len(post_data['first_name']) < 2:
            errors.append("First name must be at least two characters!")
        if not NAME_REGEX2.match(post_data['last_name']):
            errors.append("Please only use letters in your last name")
        if len(post_data['last_name']) < 2:
            errors.append('Last name must be at least two characters!')
        if len(post_data['email']) < 1:
            errors.append('Email Required')
        elif User.objects.filter(email = post_data["email"]).count() > 0:
            errors.append('Email already exists') 
        if len(post_data['password']) < 1:
            errors.append('Password is required')
        elif len(post_data['password']) < 8:
            errors.append('Password must be at least 8 characters')
        elif (post_data['password']) != (post_data['confirm']):
            errors.append('Password and Password Confirm do not match')
        return errors

    def login_validate(self, post_data):
        errors = []
        if User.objects.filter(email=post_data['email']):
            currentuser = User.objects.get(email=post_data['email'])
            db_password = currentuser.password
            if not bcrypt.checkpw(post_data['password'].encode(), db_password.encode()):
                errors.append("Invalid Password. Please try again")
        else:
            errors.append("You are not a registered user, please register!!!")
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)                                  
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()

# class LoginUser(models.Model):
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     objects=UserManager()





