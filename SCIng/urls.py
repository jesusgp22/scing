import autocomplete_light
from django.conf.urls import patterns, include, url
from django.contrib import admin

from SCIng import settings


autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SCIng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),)