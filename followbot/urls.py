""" Default urlconf for followbot """

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/$', admin.site.admin_view(admin.site.index)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'template_name': 'registration/login.html'},
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),
    (r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^', include('debug_toolbar_user_panel.urls')),
    url(r'^bad/$', bad),
    # Internal App urls
    url(r'^users/', include('bot.urls')),
    url(r'', include('base.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
