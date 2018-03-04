from __future__ import unicode_literals
from django.db import migrations, models
from django.core.validators import RegexValidator
import re
import bcrypt
import time as tt
import datetime as dt
from datetime import datetime, date, time
from django.views.generic.dates import TodayArchiveView
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import views as auth_views


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

class AppointmentManager(models.Manager):
    def appointmentvalidate(self, post_data):
        errors = []
        print "DATE"
        date = post_data['date']
        print date
        print (type(date))
        # 
        print "DATECONVERT"
        dateconvert = datetime.strptime(date, '%Y-%m-%d')
        print dateconvert
        print (type(dateconvert))
        #
        time = post_data['time']
        timeconvert = datetime.strptime(time, '%H:%M').time()
        dtcombo = datetime.combine(dateconvert, timeconvert)
        print dtcombo
        #
        print "TODAY"
        today = dt.datetime.today()
        print today
        print (type(today))
        #
        if dtcombo <= today:
            errors.append('Appointment date must occur after or on current date')
        if len(post_data['time']) == 0:
            errors.append('Appointment Time Requred')
        if len(post_data['task']) < 1:
            errors.append('Appointment Task Information Required')
        return errors

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    date = models.DateField('Appointment Date', blank=True, null=True)
    time = models.TimeField('Appointment Time', auto_now_add=False, null=True)
    status = models.CharField(max_length=255)
    userid = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = AppointmentManager()
