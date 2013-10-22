from celery import task
from users.models import User, Follower
from bot.models import Query, Favorite, DeltaFollower
from twitter import Twitter, OAuth, TwitterHTTPError

@task()
def favorite():   
    #user.socialaccount_set.get(provider='twitter').extra_data

    print "favorite"