from django.db import models
from decimal import Decimal
from users.models import User

class Grammar(models.Model):
    # NLP Context-Free Grammar
    grammar = models.CharField(max_length=140)

# Unified lowercase noun and verb phrase keywords
# that the user has in a query
class Keyword(models.Model):
    keyword = models.CharField(max_length=140)
    
    # NLP Context-Free Grammar for this keyword
    grammar = models.ForeignKey(Grammar)

    #bid = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
    
    def __unicode__(self):
        return self.keyword

# Users search query for favorites
class Query(models.Model):
	# Formatted query to how the user wanted
    query = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

    bid = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))

    keywords = models.ManyToManyField(Keyword)

    def __unicode__(self):
        return self.query

# Log for campaigns
class Campaign(models.Model):
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField()

    # Daily campaign cycle number (eg. 1-5)
    cycle = models.IntegerField()
    date = models.DateField(auto_now_add=True)

# Log for found tweets
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    tweetId = models.BigIntegerField()
    twitterUserId = models.BigIntegerField()
    # Time Tweet was published
    time = models.DateTimeField()

    keywords = models.ManyToManyField(Keyword)

    def __unicode__(self):
        return self.tweet

# Log for favorites
class Favorite(models.Model):
    query = models.ForeignKey(Query)
    tweet = models.ForeignKey(Tweet)
    campaign = models.ForeignKey(Campaign)
    #Time tweet was favorited
    time =  models.DateTimeField(auto_now_add=True)

    # Was the favorite deleted, not the tweet
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.tweet.tweetId + " " + self.tweet.twitterUserId

# User's twitter followers
class Follower(models.Model):
    user = models.ForeignKey(User)  
    twitterUserId = models.BigIntegerField()

    # For delta followers
    favorite = models.ForeignKey(Favorite, blank=True)
    dateFollowed = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username + " " + self.twitterUserId