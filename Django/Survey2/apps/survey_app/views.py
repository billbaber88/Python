# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response ="working"
    return render(request, 'survey_app/index.html')

def process(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] += 1

    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    request.session['count'] += 1

    return redirect('/result')

def result(request):
    return render(request, 'survey_app/result.html')
