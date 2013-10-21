from django.db import models
from users.models import User

# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=140)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.keyword

class Tweet(models.Model):
    keyword = models.ForeignKey(Keyword)
    user = models.ForeignKey(User)	
    favoritedTime =  models.DateTimeField(auto_now_add=True)

    favorited = models.BooleanField()
    favoriteDeleted = models.BooleanField()

    tweetId = models.CharField(max_length=15)
    tweetTime = models.DateTimeField()
    twitterUserId = models.CharField(max_length=15)
    
    def __unicode__(self):
        return tweetId + " " + twitterUser