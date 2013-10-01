"""urlconf for the bot application"""
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from bot.views import HomeView


urlpatterns = patterns('bot.views',
    url(r'^(?P<slug>\w+)/$', login_required(HomeView.as_view()),
        name="profile"),
)
