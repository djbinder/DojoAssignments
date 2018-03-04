# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
from datetime import datetime, date, timedelta
from django.views.generic.dates import TodayArchiveView


def index(request):
    if "userid" in request.session:  
        userid = request.session['userid']
        return redirect('/dashboard')
    else:                           
        return render(request, 'beltapp/index.html') 

def createuser(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        hashmasterflash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) 
        newuser = User.objects.create(
            name=request.POST['name'],
            username=request.POST['username'],
            password=hashmasterflash,
            hiredate=request.POST['hiredate'],
            )
        request.session['userid'] = newuser.id
        # request.session['name'] = newuser.name
        return render(request, 'beltapp/dashboard.html')

def login(request):
    errors = User.objects.loginvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.filter(username=request.POST['username'])[0]
        request.session['userid'] = user.id
        request.session['name'] = user.name
        return render(request, 'beltapp/dashboard.html', context)

def dashboard(request):
    userid=request.session['userid']
    currentUser=User.objects.get(id=userid)
    context = {
        'items': Item.objects.all(),
        'wishes': currentUser.userWishes.all()
        # 'name': name
    }
    return render(request, 'beltapp/dashboard.html', context)

def viewwishers(request, id):
    item_list = Item.objects.filter(id=id)
    if len(item_list) > 0:
        item = item_list[0]
        id_get = item.id
    context = {
        'users': User.objects.all(),
        'item': item.name,
        'id': id_get
    }
    return render(request, 'beltapp/wishers.html', context)

def show(request, id):
    userid=request.session['userid']
    currentUser=User.objects.get(id=id)
    print currentUser
    # userid=request.session['userid']
    # print currentUser
    wishes=currentUser.userWishes.all()
    items = items.objects.all()
    name = 'dan'
    context = {
        'items': items,
        'item': items.objects.all(),
        'name': name,
        'wishes': wishes,
        # 'userid': userid
    }
    return render(request, 'beltapp/dashboard.html', context)

def wish(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    print currentUser
    print currentUser.id
    wish = Item.objects.get(id=id)
    print wish
    wish.wishes.add(currentUser)
    wish.save()
    return redirect('/dashboard')

def createitemview(request):
    return render(request, 'beltapp/createitem.html')

def createitem(request):
    errors = Item.objects.validateitem(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/createitem')
    else:
        userid=request.session['userid']
        Item.objects.create(
            name = request.POST['name'],
            userid = userid,
        )
        return redirect('/createitemview')

def destroy(request, id):
    item = Item.objects.filter(id=id)
    item.delete()
    return redirect('/')

def delete(request, id):
    item_list = Item.objects.filter(id=id)
    if len(item_list) > 0:
        item = item_list[0]
        name = item.name
        id = item.id
        context = {
            'name': name, 
            'id': id, 
        }
    return render(request, 'beltapp/delete.html', context)

def logout(request, methods='POST'):
    request.session.clear() 
    return redirect('/')
