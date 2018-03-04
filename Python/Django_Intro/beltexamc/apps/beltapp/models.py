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
        if not NAME_REGEX2.match(post_data['name']):
            errors.append("Please only use letters in your name")
        if len(post_data['name']) < 3:
            errors.append("Name must be at least three characters!")
        if len(post_data['alias']) < 3:
            errors.append("Alias must be at least three characters")
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
        if (post_data['birthdate']) <0:
            errors.append('Birthdate is Requred')
        return errors

    def loginvalidate(self, post_data):
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
    name = models.CharField(max_length=255)               
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()


class QuoteManager(models.Manager):
    def validatequote(self, post_data):
        errors = []
        if len(post_data['author']) < 4:
            errors.append('Quoted by must be more than 3 characters')
        if len(post_data['quote']) < 11:
            errors.append('Quote must be more than 10 characters')
        return errors


class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    favorite = models.ManyToManyField(User, related_name='favorite')
    created_by = models.ForeignKey(User, related_name='creator')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
