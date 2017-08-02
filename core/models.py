# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField


class MainPage(models.Model):
    title = models.CharField(max_length=80, verbose_name=u"Заголовок")
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")

    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'

    class Meta:
        db_table = 'main_page'
        verbose_name = u'Главная страница'
        verbose_name_plural = u'Главная страница'


class Photo(models.Model):
    #title = models.CharField(max_length=80, verbose_name=u"Название")
    image = ImageField(upload_to='photos', verbose_name=u"Фотография")

    class Meta:
        db_table = 'photos'
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'