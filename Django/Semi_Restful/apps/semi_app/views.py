# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'semi_app/index.html', context )

def new(request):
    
    return render(request, 'semi_app/newuser.html')

def create(request):
    errors = User.objects.user_validate(request.POST)
    if len(errors) <= 0:
        # first_name = request.POST['first_name'],
        # last_name = request.POST['last_name'],
        # new_email = request.POST['email']
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    else:
        for x in errors:
            messages.error(request, errors[x])

    return redirect('/semi_app')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_app/edit.html', context)

def update(request, user_id):
    errors = User.objects.user_validate(request.POST)
    if len(errors) <= 0:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        return redirect('/semi_app')
#####
    else:
        for x in errors:
            messages.error(request, errors[x])

    
    return redirect('/semi_app')
    
def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_app/show.html/', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/semi_app')