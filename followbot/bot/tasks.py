from celery import task
from twitter import Twitter, OAuth, TwitterHTTPError
from datetime import datetime

from random import sample, choice

from django.db.models import Count

from users.models import User
from bot.models import Query, Campaign, Favorite, Follower

MAX_FAVORITES = 10

@task()
def campaign(cycle):
    campaign = Campaign(cycle=cycle)
    campaign.save()

    users = User.objects.filter(is_active=True).filter(Query__deleted=False).annotate(num_queries=Count('Query')).filter(num_queries__gt=0)
    #print users.query
    for user in users:
        twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        queries = user.query_set.filter(deleted=False)
        pickedQueries = []
        if(queries.count() > MAX_FAVORITES):
            pickedQueries = sample(queries, MAX_FAVORITES)
        else:
            pickedQueries = queries

        for query in pickedQueries:
            print query.query
            tweets = query.tweet_set.filter(favorite__isnull=True)
            if len(tweets) > 0:
                favorite(choice(tweets))
            else:    
                search(twitter, query)

    #Query.objects.filter(deleted=False).order_by('-bid')
    #user.socialaccount_set.get(provider='twitter').extra_data

    campaign.endTime = datetime.now()
    campaign.save()

    print "campaign"

def search(twitter, q, count=100):
    return twitter.search.tweets(q=q, result_type='recent', count=count, lang="en")

def favorite(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: %s, %s" % (result['text'], result['id'])
        return result
    except TwitterHTTPError as e:
        print "Error: ", e
        return None
    
@task()
def feedback():
    print "feedback"