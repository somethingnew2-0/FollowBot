# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username

class Follower(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)	
    twitterUser = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return user.username + " " + twitterUser