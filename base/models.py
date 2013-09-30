# -*- coding: utf-8 -*-

""" Basic models, such as user profile """
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), unique=True,
        related_name='profile')

    # Extra attributes ...

    def __unicode__(self):
        return "{0}'s profile".format(self.user)


def create_profile(sender, instance, created, **kwargs):
    '''Signal handler that ensures that a UserProfile is created
    whenever a User is created.
    '''
    created = False
    if created:
        profile, created = \
            UserProfile.objects.get_or_create(user=instance)
    return created


post_save.connect(create_profile, sender=get_user_model())
