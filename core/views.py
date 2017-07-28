# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import MainPage


def index(request):
    return render(request, 'index.html', {'main_page': MainPage.objects.first()})


def photos(request):
    return render(request, 'photos.html')


def videos(request):
    return render(request, 'videos.html')
