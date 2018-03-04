from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from time import gmtime, strftime, localtime


def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'time_display_app/index.html', context)

def time_display(request):
    return redirect ("/")

def page(request):
    context = {
    "time": strftime("%b %d, %Y %I:%M%p")
    }
    return render(request,'time_display_app/page.html', context)



