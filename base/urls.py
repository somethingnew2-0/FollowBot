"""urlconf for the base application"""
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from base.views import HomeView, UserProfileDetailView


urlpatterns = patterns('base.views',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^users/(?P<slug>\w+)/$', login_required(UserProfileDetailView.as_view()),
        name="profile"),
)
