from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    return render(request, 'ninjagold_app/index.html')

def process(request):
    if request.method=='POST':
        gold_count = request.session.get('gold_count', 0)
        request.session['gold_count'] = gold_count

        message = request.session.get('message', 0)
        request.session['message'] = message

        location = request.POST['location']

        if location == "farm":
            added_gold = random.randrange(10,21)
            request.session['message'] = "you win money from the farm" 
            request.session['gold_count'] = request.session['gold_count'] + added_gold

        if location =="cave":
            added_gold = random.randrange(5,10)
            request.session['message'] = "you win money from the cave" 
            request.session['gold_count'] = request.session['gold_count'] + added_gold

        if location =="house":
            added_gold = random.randrange(2,5)
            request.session['message'] = "you win money from the house"
            request.session['gold_count'] = request.session['gold_count'] + added_gold

        if location =="casino":
            added_gold = random.randrange(-50,50)
            request.session['message'] = "you win money from the casino "
            request.session['gold_count'] = request.session['gold_count'] + added_gold

        context = {
            'gold_count': gold_count,
            'message': message,
            'location': location
        }

    return redirect('/')

# def results(request):
#     return render(request, 'ninjagold_app/index.html')
    






# return render(request, 'ninjagold_app/index.html', context)

# def choice(request):
#     return render(request, 'ninjagold_app/index.html')