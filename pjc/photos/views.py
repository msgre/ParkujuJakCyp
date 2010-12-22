# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.simple import direct_to_template
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404

from pjc.photos.models import Photo
from pjc.photos.forms import PhotoForm


RECENT_PHOTOS = 3
PHOTOS_PER_PAGE = 10


def homepage(request):
    """
    Uvodni stranka s upload formikem.
    """
    # osetreni formulare a ulozeni nove fotky
    if request.POST:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            messages.add_message(request, messages.INFO, u'Fotka se nahrála. Dík jak cyp!')
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = PhotoForm()

    # sup do sablony
    photos = Photo.objects.public()[:RECENT_PHOTOS+1]
    return direct_to_template(
        request,
        template = 'photos/homepage.html',
        extra_context = {
            'object_list': photos[:RECENT_PHOTOS],
            'next_page': len(photos) > RECENT_PHOTOS,
            'homepage': True,
            'form': form
        }
    )


def photos_list(request, page):
    """
    Strankovany seznam fotek.
    """
    # strankovani
    try:
        page = int(page)
    except:
        page = 1

    # sup do sablony
    return object_list(
        request,
        queryset = Photo.objects.public(),
        paginate_by = PHOTOS_PER_PAGE,
        page = page,
        template_name = "photos/photos_list.html",
    )


def photos_detail(request, id):
    """
    Detail fotky.
    """
    try:
        id = int(id)
    except:
        raise Http404

    return object_detail(
        request,
        queryset = Photo.objects.public(),
        object_id = id,
        template_name = "photos/photos_detail.html",
    )
