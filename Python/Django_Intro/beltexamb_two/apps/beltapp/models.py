# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
from django.core.validators import RegexValidator
import re
import bcrypt
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import views as auth_views

NAME_REGEX2 = re.compile(r'^([a-zA-Z ]*)$')

class UserManager(models.Manager):
    def validate(self, post_data): 
        errors = []
        if not NAME_REGEX2.match(post_data['myname']):
            errors.append("Please only use letters in your name")
        if len(post_data['myname']) < 3:
            errors.append("Name must be at least three characters!")
        if len(post_data['myusername']) < 3:
            errors.append("Username must be at least three characters")
        if len(post_data['password']) < 1:
            errors.append('Password is required')
        elif len(post_data['password']) < 8:
            errors.append('Password must be at least 8 characters')
        elif (post_data['password']) != (post_data['confirm']):
            errors.append('Password and Password Confirm do not match')
        if (post_data['hiredate']) <0:
            errors.append('Hire Date is Requred')
        return errors

    def loginvalidate(self, post_data):
        errors = []
        if User.objects.filter(myusername=post_data['myusername']):
            currentuser = User.objects.get(myusername=post_data['myusername'])
            db_password = currentuser.password
            if not bcrypt.checkpw(post_data['password'].encode(), db_password.encode()):
                errors.append("Invalid Password. Please try again")
        else:
            errors.append("You are not a registered user, please register!!!")
        return errors

class User(models.Model):
    myname = models.CharField(max_length=255)               
    myusername = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hiredate = models.DateField('Hire Date', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()


class ItemManager(models.Manager):
    def validateitem(self, post_data):
        errors = []
        if len(post_data['itemname']) < 1:
            errors.append('Item/Product name required')
        elif len(post_data['itemname']) < 4:
            errors.append('Item/Product name must be more than 3 characters')
        return errors

class Item(models.Model):
    itemname = models.CharField(max_length=14)
    add_to_list_user = models.ForeignKey(User, related_name='userAdds')
    wishitems = models.ManyToManyField(User, related_name='userWishes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()