from django.db import models
from users.models import User, Follower

# Keywords that the user has selected
class Keyword(models.Model):
    keyword = models.CharField(max_length=140)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.keyword

# Log for favorites done
class Favorite(models.Model):
    keyword = models.ForeignKey(Keyword)
    user = models.ForeignKey(User)	
    favoritedTime =  models.DateTimeField(auto_now_add=True)

    # Was the favorite deleted, not the tweet
    deleted = models.BooleanField()

    tweetId = models.BigIntegerField()
    tweetTime = models.DateTimeField()
    twitterUserId = models.BigIntegerField()
    
    def __unicode__(self):
        return tweetId + " " + twitterUserId

# Log for new followers
class DeltaFollower(models.Model):
    follower = models.ForeignKey(Follower)
    favorite = models.ForeignKey(Favorite, blank=True)
    dateFollowed = models.DateField(auto_now_add=True)