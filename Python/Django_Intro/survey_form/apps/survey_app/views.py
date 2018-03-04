from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'survey_app/index.html')

def process(request):
    request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/results')

def results(request):
    return render(request, 'log_reg_app/success.html')




    # if action = create do x, if it = login do y