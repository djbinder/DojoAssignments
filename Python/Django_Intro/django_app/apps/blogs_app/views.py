#DJANGO_APP

from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect



def index(request):                                                         
    return render(request, "blogs_app/index.html")

def new(request):                                                         
    return render(request, "blogs_app/new.html")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")


def show(request,number):
    return HttpResponse("Placeholder to display blog " + number)

def edit(request,number):
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request,number):
    return HttpResponseRedirect('/')