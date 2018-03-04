from __future__ import unicode_literals
from django.db import migrations, models
from django.core.validators import RegexValidator
import re
import bcrypt
import time as tt
import datetime as dt
from datetime import datetime, date, time
# from django.views.generic.dates import TodayArchiveView
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

NAME_REGEX2 = re.compile(r'^([a-zA-Z ]*)$')

class UserManager(models.Manager):
    def validate(self, post_data): 
        errors = []
        if not NAME_REGEX2.match(post_data['name']):
            errors.append("Please only use letters in your name")
        if len(post_data['name']) < 2:
            errors.append("Name must be at least two characters!")
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
        if (post_data['birth_date']) <0:
            errors.append('Birth Date is Requred')
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
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField('Date of Birth', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['coursename']) < 6:
            errors.append('Course name is too short. It must be at least 6 characters long')
        if len(post_data['coursename']) > 14:
            errors.append('Course name is too long. Course names must be no more than 14 characters long')
        if len(post_data['description']) < 16:
            errors.append('Course description is too short. It must be at least 15 characters long')
        return errors

class Course(models.Model):
    coursename = models.CharField(max_length=14)
    description = models.CharField(max_length=255)
    userid = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, related_name="userFavorites")
    userAdded = models.ForeignKey(User, related_name="userAdds")
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = CourseManager()