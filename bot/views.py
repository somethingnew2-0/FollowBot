from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from base.models import UserProfile
from twitter import Twitter, OAuth, TwitterHTTPError
from tweetbot.settings import *

# Create your views here.
class HomeView(TemplateView):
    '''Default view for the root.'''
    template_name = "bot/home.html"

    t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

    def search_tweets(q, count=100, max_id=None):
        return t.search.tweets(q=q, result_type='recent', count=count, lang="en", max_id=max_id)

    def favorites_create(tweet):
        try:
            result = t.favorites.create(_id=tweet['id'])
            print "Favorited: %s, %s" % (result['text'], result['id'])
            return result
        except TwitterHTTPError as e:
            print "Error: ", e
            return None


    def search_and_fav(q, count=100, max_id=None):
        result = search_tweets(q, count, max_id)
        first_id = result['statuses'][0]['id']
        last_id = result['statuses'][-1]['id']
        success = 0
        for t in result['statuses']:
            if favorites_create(t) is not None:
                success += 1

        print "Favorited total: %i of %i" % (success, len(result['statuses']))
        print "First id %s last id %s" % (first_id, last_id)