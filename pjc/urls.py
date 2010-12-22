import os

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pjc.photos.views.homepage', name="homepage"),
    url(r'^g/(?P<page>\d+)/$', 'pjc.photos.views.photos_list', name="photos-list"),
    url(r'^d/(?P<id>\d+)/$', 'pjc.photos.views.photos_detail', name="photos-detail"),
    url(r'^proc/$', 'django.views.generic.simple.direct_to_template', {'template': 'static/proc.html'}, name="proc"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, '')}),
    )
