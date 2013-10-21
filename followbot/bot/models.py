from django.db import models
from users.models import User

# Create your models here.
class Keyword(models.Model):
    keyword = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, null=False, blank=False)

    def __unicode__(self):
        return self.keyword

class Tweet(models.Model):
    keyword = models.ForeignKey(Keyword, blank=False, null=False)
    user = models.ForeignKey(User, null=False, blank=False)	
    tweetId = models.TextField(blank=False, null=False)
    twitterUser = models.TextField(blank=False, null=False)
    