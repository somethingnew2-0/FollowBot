from django.db import models
from decimal import Decimal
from users.models import User, Follower

# Users custom query
class Query(models.Model):
	# Formatted query to how the user wanted
    query = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

    #bid = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))

    def __unicode__(self):
        return self.query

# Unified lowercase keywords that the user 
# has selected which are in a query
class Keyword(models.Model):
    keyword = models.CharField(max_length=140)
    term = models.ForeignKey(Query)

    #bid = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
    def __unicode__(self):
        return self.keyword

# Log for favorites done
class Favorite(models.Model):
    query = models.ForeignKey(Query)
    favoritedTime =  models.DateTimeField(auto_now_add=True)

    # Was the favorite deleted, not the tweet
    deleted = models.BooleanField(default=False)

    tweetId = models.BigIntegerField()
    tweetTime = models.DateTimeField()
    twitterUserId = models.BigIntegerField()
    
    def __unicode__(self):
        return self.tweetId + " " + self.twitterUserId

# Log for new followers
class DeltaFollower(models.Model):
    follower = models.ForeignKey(Follower)
    favorite = models.ForeignKey(Favorite, blank=True)
    dateFollowed = models.DateField(auto_now_add=True)