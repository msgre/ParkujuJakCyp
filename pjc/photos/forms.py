# -*- coding: utf-8 -*-

from django import forms
from django.template.defaultfilters import filesizeformat

MAX_UPLOAD_SIZE = 5242880 # 5 MB


class PhotoForm(forms.Form):
    """
    Jednoduchy formik pro upload souboru.
    """
    photo = forms.ImageField(label=u"Soubor")

    def clean_photo(self):
        """
        Overeni maximalni velikosti uploadovaneho souboru.
        """
        photo = self.cleaned_data['photo']
        if photo.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError(u'Pokoušíš se nahrát móc velkou fotku. Zkus ji zmenšit pod %s.' % \
                                        filesizeformat(MAX_UPLOAD_SIZE))
        return photo

    def save(self, request):
        """
        Ulozeni nove uploadnute fotky.
        """
        from pjc.photos.models import Photo
        photo = Photo.objects.create(
            photo      = self.cleaned_data['photo'],
            ip         = request.META.get('REMOTE_ADDR', None),
            user_agent = request.META.get('HTTP_USER_AGENT', None)
        )
        return photo
