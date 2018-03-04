from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.contrib.messages import error
from datetime import datetime, date, timedelta
from django.views.generic.dates import TodayArchiveView



#********************INDEX********************
def index(request):
    print '**********INDEX**********'
    if "userid" in request.session:
        return redirect('/home')
    else:
        return render(request, 'beltapp/index.html')





#********************CREATEUSER********************
def createuser(request):
    print '**********CREATEUSER**********'
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        hashmasterflash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) 
        newuser = User.objects.create(
            name=request.POST['name'],
            alias=request.POST['alias'],
            email=request.POST['email'],
            password=hashmasterflash,
            birthdate=request.POST['birthdate'],
            )
        request.session['username'] = newuser.name
        request.session['userid'] = newuser.id     
        print 'SESSION INFO:', newuser.id, newuser.name                           
        return redirect('/home')





#********************LOGIN********************
def login(request):
    print '**********LOGIN**********'
    errors = User.objects.loginvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        print '**********LOGIN ELSE**********'
        user = User.objects.filter(email=request.POST['email'])[0]
        request.session['userid'] = user.id                    
        request.session['name'] = user.name
        print 'SESSION INFO:', user.id, user.name
        return redirect('/home')





#********************VIEW HOME*******************
def home(request):
    print "**********HOME**********"
    userid = request.session['userid']                          
    user = User.objects.get(id=userid)   
    favorite = user.favorite.all() 
    context = {
        'name': user.name, 
        'favorites': favorite,
        'otherquotes': Quote.objects.exclude(favorite=userid)
    }                                      
    return render(request, 'beltapp/home.html', context)






#********************ADD FAVORITE*******************
def addfavorite(request, id):
    print "**********ADD FAVORITE**********"
    userid = request.session['userid']
    myfavorite = Quote.objects.get(id=id)
    myfavorite.favorite.add(userid)
    myfavorite.save()
    return redirect('/home')





#********************REMOVE FAVORITE*******************
def removefavorite(request, id):
    print "**********REMOVE FAVORITE**********"
    userid = request.session['userid']
    myfavorite = Quote.objects.get(id=id)
    myfavorite.favorite.remove(userid)
    myfavorite.save()
    return redirect('/home')






#********************ADD QUOTE*******************
def addquote(request):
    print "**********ADD QUOTE*********"
    errors = Quote.objects.validatequote(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/home')
    else:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        Quote.objects.create(
            author=request.POST['author'],
            quote=request.POST['quote'],
            created_by=user
        )
        return redirect('/home')





#********************USER*******************
def users(request, id):
    print "**********USER*********"
    currentUser = User.objects.get(id=id)
    print currentUser.name
    quote_list = Quote.objects.filter(created_by=currentUser)
    count = Quote.objects.filter(created_by=currentUser).count()
    print count
    print quote_list
    context = {
        'name': currentUser.name,
        'quotes': Quote.objects.filter(created_by=currentUser),
        'count': count
        # 'quote': quote.quote,
        # 'author': quote.author
    }
    return render(request, 'beltapp/users.html', context)








#********************LOGOUT*******************
def logout(request, methods='POST'):
    print "***************LOGOUT***************"
    request.session.clear() 
    return redirect('/')