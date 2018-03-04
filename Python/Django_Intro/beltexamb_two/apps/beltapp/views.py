from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.contrib.messages import error
# from datetime import datetime, date, timedelta
# from django.views.generic.dates import TodayArchiveView



def index(request):
    if "userid" in request.session:  
        print "*****INDEX USERID IN SESSION*****"
        return redirect('/viewdashboard')
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
            myname=request.POST['myname'],
            myusername=request.POST['myusername'],
            password=hashmasterflash,
            hiredate=request.POST['hiredate'],
            )
        print "*****CREATE USER ELSE*****"
        request.session['myusername'] = newuser.myusername         # sets username for the session to the users myusername
        # print myusername
        request.session['userid'] = newuser.id                                      # sets userid for the session to the uses id
        # print userid
        return redirect('/viewdashboard')


def login(request):
    errors = User.objects.loginvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        print "*****LOGIN ELSE*****"
        user = User.objects.filter(myusername=request.POST['myusername'])[0]
        request.session['userid'] = user.id                     # this sets the userid for the session
        request.session['myname'] = user.myname
        request.session['myusername'] = user.myusername
        print user.id
        print user.myname
        print user.myusername
        return redirect('/viewdashboard')

def viewdashboard(request):
    print "*****VIEWDASHBOARD*****"
    userid = request.session['userid']                          
    currentUser = User.objects.get(id=userid)                                                
    userid = currentUser.id                                                            
    wishes = currentUser.userWishes.all()                                                   
    context = {
        'wishes': wishes,
        'otheritems': Item.objects.exclude(wishitems=userid)
    }
    return render(request, 'beltapp/dashboard.html', context)

def viewadditem(request):
    print "*****VIEWADDITEM*****"
    return render(request, 'beltapp/additem.html')

def additem(request):
    print "*****ADDITEM*****"
    errors = Item.objects.validateitem(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/viewadditem')
    else:
        userid=request.session['userid']
        print "*****ADDITEM ELSE*****"
        print userid
        Item.objects.create(
            itemname=request.POST['itemname'],
            add_to_list_user_id=userid,
        )
        return redirect('/viewdashboard')

def addwish(request, id):
    print "*****ADDWISH*****"
    print "*****CURRENTUSER*****"
    currentUser = User.objects.get(id=request.session['userid'])
    print currentUser
    print "*****USERID*****"
    userid=request.session['userid']
    print userid
    print "*****WISH*****"
    wish = Item.objects.get(id=id)
    print wish
    wish.wishitems.add(currentUser)
    wish.save()
    return redirect('/viewdashboard')

def removewish(request, id):
    print "*****REMOVEWISH*****"
    currentUser = User.objects.get(id=request.session['userid'])
    userid=request.session['userid']
    wish = Item.objects.get(id=id)
    wish.wishitems.remove(currentUser)
    wish.save()
    return redirect('/viewdashboard')

def allwishers(request, id):
    item = Item.objects.get(id=id)
    print item
    users = item.wishitem.all()
    print users
    creator = item.wishitem.name
    print owner
    context = {
        'item': item
    }
    return render(request, 'beltapp/allwishers.html', context)

def destroy(request, id):
    wish = Item.objects.get(id = id)
    wish.delete()
    return redirect('/viewdashboard')

def logout(request, methods='POST'):
    print "*****LOGOUT*****"
    request.session.clear() 
    return redirect('/')