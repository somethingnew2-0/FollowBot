# -*- coding: utf-8 -*-

import factory

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from base.models import UserProfile, create_profile


class UserProfileFactory(factory.DjangoModelFactory):

    FACTORY_FOR = UserProfile
    FACTORY_DJANGO_GET_OR_CREATE = ('user',)


class UserFactory(factory.DjangoModelFactory):

    FACTORY_FOR = get_user_model()
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    username = factory.Sequence(lambda n: 'borg_{0}'.format(n))
    first_name = factory.Sequence(lambda n: 'first_{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'last_{0}'.format(n))
    email = factory.Sequence(lambda n: 'user_{0}@example.com'.format(n))
    is_active = True
    is_staff = False
    is_superuser = False
    password = factory.PostGenerationMethodCall('set_password', 'password')

    profile = factory.RelatedFactory(UserProfileFactory, 'user')

    @classmethod
    def create(_class, **kwargs):
        '''Override create() method to disable post_save signal that creates
        a user profile before creating the new User instance.
        '''
        user_model = get_user_model()
        post_save.disconnect(create_profile, user_model)  # Disconnect signal
        results = super(UserFactory, _class).create(**kwargs)
        post_save.connect(create_profile, user_model)  # Reconnect signal
        return results
