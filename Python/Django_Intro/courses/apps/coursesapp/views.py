from __future__ import unicode_literals
import json
from django.shortcuts import render, redirect
from .models import *
from .models import Course
from django.contrib import messages, auth
from django.contrib.messages import error
from django.views import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse




def index(request):
    if 'userid' in request.session:
        return redirect('/courses')
    else:
        return render(request, 'coursesapp/index.html')

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
            email=request.POST['email'],
            password=hashmasterflash,
            birth_date=request.POST['birth_date'],
            )
        request.session['userid'] = newuser.id
        request.session['name'] = newuser.name
        return render(request, 'courses.html')

def login(request):
    errors = User.objects.loginvalidate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])[0]
        request.session['userid'] = user.id
        return redirect('/courses')

def show(request):
    currentuser=request.session['userid']
    # course=Course.objects.all()
    # print currentuser
    # print course
    context = {
        'courses': Course.objects.all(),
        'userid': currentuser
    }
    return render(request, 'coursesapp/courses.html', context)

def createcourse(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        userid=request.session['userid']
        Course.objects.create(
            coursename = request.POST['coursename'],
            description=request.POST['description'],
            userid=userid,
            userAdded_id=userid
        )
        return redirect('/')

def profile(request, id):
    print "CURRENT USER"
    currentUser = User.objects.get(id=id)
    print currentUser
    favorites = currentUser.userFavorites.all()
    # first_favorite = favorites[0]
    # print "FIRST FAVORITE"
    # print first_favorite
    # print "FAVORITES"
    # print favorites
    # print "FAVFILTER"
    # favfilter = currentUser.userFavorites.filter(favorites=2)
    # print favfilter
    # print course_favorites
    context = {
        "favorites" : favorites
    }
    return render(request,'coursesapp/profile.html', context)

def favorite(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    favorite = Course.objects.get(id=id)
    favorite.favorites.add(currentUser)
    favorite.save()
    return redirect('/courses')
    # return redirect('/profile')

def unfavorite(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    favorite = Course.objects.get(id=id)
    favorite.favorites.remove(currentUser)
    favorite.save()
    return redirect('/profile')

def destroy(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')

def delete(request, id):
    course = Course.objects.get(id = id)
    print course
    coursename = course.coursename
    description = course.description
    id = course.id
    print id
    context = {
        'coursename': coursename,
        'description': description,
        'id': id, 
    }
    return render(request, 'coursesapp/delete.html', context)

def logout(request, methods='POST'):
    request.session.clear() 
    return redirect('/')




#     def addFaves(request, id):
#     currentUser = User.objects.get(id=request.session['userid'])
#     fave = Course.objects.get(id=id)
#     fave.favorites.add(currentUser)
#     fave.save()
#     return redirect(reverse('courses:profile', args=(currentUser.id,)))

# def unfave(request, id):
#     currentUser = User.objects.get(id=request.session['userid'])
#     fave = Course.objects.get(id=id)
#     fave.favorites.remove(currentUser)
#     fave.save()
#     return redirect(reverse('courses:profile', args=(currentUser.id,)))



