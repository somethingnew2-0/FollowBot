""" Views for the base application """

from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from base.models import UserProfile

class HomeView(TemplateView):
    '''Default view for the root.'''
    template_name = "base/home.html"


class UserProfileDetailView(DetailView):
    '''User profile view.'''
    model = get_user_model()
    slug_field = "username"
    template_name = 'registration/user_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        '''Ensures that a UserProfile exists for every user.'''
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

