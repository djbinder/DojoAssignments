from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views


def index(request):
    # context = {}
    # if 'userid' in request.session:
    #     user = User.objects.filter(id=request.session['userid'])
    #     if len(user) > 0:
    #         message = str("You are currently logged in")
    #         context = {
    #             'message': message
    #         }
    #         return redirect('/success')
    #     else:
    #         del request.session['userid']
    #         message = str("You are currently logged in")
    #         context = {
    #             'message': message
    #         }
    return render(request, "log_reg_app/index.html")

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        hashmasterflash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) 
        newuser = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashmasterflash
            )
        request.session['userid'] = newuser.id
        request.session['first_name'] = newuser.first_name
        first_name = request.POST['first_name']
        message = str("You have successfully registered")
        context = {
            "first_name": first_name,
            "message": message
        }
        return render(request, 'log_reg_app/success.html', context)

def login(request):
    errors = User.objects.login_validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])[0]
        request.session['userid'] = user.id
        request.session['first_name'] = user.first_name
        return redirect("/success")

def logout(request, methods='POST'):
    request.session.clear() #clears session
    return redirect('/')

def success(request):
    user = request.session['userid']
    return render(request, 'log_reg_app/success.html' )