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
    user = models.ForeignKey(User)	
    twitterUserId = models.CharField(max_length=15)

    def __unicode__(self):
        return user.username + " " + twitterUser

class DeltaFollower(models.Model):
    from bot.models import Tweet

    follower = models.ForeignKey(Follower)
    favoritedTweet = models.ForeignKey(Tweet)
    dateFollowed = models.DateField(auto_now_add=True)