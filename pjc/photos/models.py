# -*- coding: utf-8 -*-

import os
import random
import hashlib
from datetime import datetime

from django.db import models
from django.conf import settings

from pjc.core.managers import manager_from
from pjc.photos.managers import public as public_manager


def upload_to_handler(instance, filename):
    """
    Vygeneruje cestu vcetne jmena souboru, do ktereho bude uploadnuty
    obrazek nahran.
    """
    # vygenerujeme nazev souboru
    n = datetime.now().isoformat()
    r = random.randint(0, 1000)
    name = hashlib.sha1(n + str(r)).hexdigest().lower()
    # pokusime se najit priponu souboru
    ext = ''
    if '.' in filename:
        parts = filename.split('.')
        name = "%s.%s" % (name, parts[-1].lower())
    # vratime cestu
    return os.path.join(settings.PHOTO_UPLOAD_DIR, name)


class Photo(models.Model):
    """
    Uploadnuta fotka.
    """
    photo      = models.ImageField(u"Fotka", upload_to=upload_to_handler, \
                                   height_field="height", width_field="width")
    width      = models.IntegerField(u"Šířka fotky", blank=True, null=True)
    height     = models.IntegerField(u"Výška fotky", blank=True, null=True)
    ip         = models.CharField(u"IP adresa", max_length=30)
    created    = models.DateTimeField(u"Vytvořeno", auto_now_add=True)
    user_agent = models.TextField(u"User agent", blank=True, null=True)
    public     = models.BooleanField(u"Veřejná fotka", default=True)
    objects    = manager_from(public_manager)

    class Meta:
        ordering = ('-created', )
        verbose_name = u'Fotka'
        verbose_name_plural = u'Fotky'

    def __unicode__(self):
        return "ID=%i, %s" % (self.id, self.created)
