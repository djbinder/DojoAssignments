from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# from django.random import random, string


def index(request):
    return render(request, 'random_word/index.html')

def generate(request):
    num_clicks = request.session.get('num_clicks', 0)
    request.session['num_clicks'] = num_clicks + 1
    context = {
    "rando": get_random_string(length=32),
    "num_clicks": num_clicks
    }
    return render(request, 'random_word/index.html', context)
