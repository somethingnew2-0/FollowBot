# -*- coding: utf-8 -*-
'''Unit tests for the base app'''

from nose.tools import *  # PEP8 asserts
from django.test import TestCase
from django.contrib.auth.models import User

from base.models import UserProfile
from base.test.factories import UserFactory, UserProfileFactory


class UserTest(TestCase):

    '''User unit tests.'''

    def setUp(self):
        pass

    def test_factory(self):
        # Clear all Users
        User.objects.all().delete()
        # Create a new user
        user = UserFactory()
        # Check that User and UserProfile were saved to database
        assert_equal(User.objects.count(), 1)
        assert_equal(UserProfile.objects.count(), 1)
        # The user has a user profile
        assert_true(user.profile)


class UserProfileTest(TestCase):

    def setUp(self):
        pass
