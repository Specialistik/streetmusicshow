# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


class MainPage(models.Model):
    title = models.CharField(max_length=80, verbose_name=u"Заголовок")
    description = RichTextField(null=True, blank=True, verbose_name=u"Описание")
    image = ImageField(null=True, blank=True, upload_to='photos', verbose_name=u"Фотография")

    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'

    class Meta:
        db_table = 'main_page'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'


class Photo(models.Model):
    #title = models.CharField(max_length=80, verbose_name=u"Название")
    image = ImageField(upload_to='photos', verbose_name=u"Фотография")

    """
    def image_tag(self):
        return u'<img src="%s" />' % self.image.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    """

    class Meta:
        db_table = 'photos'
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'