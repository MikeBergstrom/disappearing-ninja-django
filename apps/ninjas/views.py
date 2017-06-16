# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    return render(request, 'ninjas/ninjas.html')

def display(request, color):
    print color
    if color == 'red':
        return render(request, 'ninjas/red.html')
    elif color == 'blue':
        return render(request, 'ninjas/blue.html')
    elif color == 'purple':
        return render(request, 'ninjas/purple.html')  
    elif color == 'orange':
        return render(request, 'ninjas/orange.html')  
    else:
        return render(request, 'ninjas/april.html')      

# Create your views here.
