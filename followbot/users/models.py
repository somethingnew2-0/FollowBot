# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _

# Subclass AbstractUser
class User(AbstractUser):
	# Access twitter account by 
	# self.socialaccount_set.get(provider='twitter')
    def __unicode__(self):
        return self.username

# User's twitter followers
class Follower(models.Model):
    user = models.ForeignKey(User)	
    twitterUserId = models.BigIntegerField()

    def __unicode__(self):
        return user.username + " " + twitterUserId