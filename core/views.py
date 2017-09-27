# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from models import MainPage, Photo, Video


def index(request):
    return render(request, 'index.html', {'articles': MainPage.objects.all()})


def article(request, pk):
    article_instance = get_object_or_404(MainPage, pk=pk)
    return render(request, 'article.html', {'article': article_instance})


def photos(request):
    return render(request, 'photos.html', {'photos': Photo.objects.all()})


def videos(request):
    return render(request, 'videos.html', {'videos': Video.objects.all(), 'first_video': Video.objects.first()})


def get_full_description(request, pk):
    article_instance = get_object_or_404(MainPage, pk=pk)
    return HttpResponse(article_instance.description)


def get_short_description(request, pk):
    article_instance = get_object_or_404(MainPage, pk=pk)
    return HttpResponse(article_instance.castrated_description)
