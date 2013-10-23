# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grammar'
        db.create_table(u'bot_grammar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grammar', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'bot', ['Grammar'])

        # Adding model 'Keyword'
        db.create_table(u'bot_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('grammar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Grammar'])),
        ))
        db.send_create_signal(u'bot', ['Keyword'])

        # Adding model 'Query'
        db.create_table(u'bot_query', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bid', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal(u'bot', ['Query'])

        # Adding M2M table for field keywords on 'Query'
        m2m_table_name = db.shorten_name(u'bot_query_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('query', models.ForeignKey(orm[u'bot.query'], null=False)),
            ('keyword', models.ForeignKey(orm[u'bot.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['query_id', 'keyword_id'])

        # Adding model 'Campaign'
        db.create_table(u'bot_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('cycle', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'bot', ['Campaign'])

        # Adding model 'Tweet'
        db.create_table(u'bot_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('tweetId', self.gf('django.db.models.fields.BigIntegerField')()),
            ('twitterUserId', self.gf('django.db.models.fields.BigIntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'bot', ['Tweet'])

        # Adding M2M table for field keywords on 'Tweet'
        m2m_table_name = db.shorten_name(u'bot_tweet_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'bot.tweet'], null=False)),
            ('keyword', models.ForeignKey(orm[u'bot.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'keyword_id'])

        # Adding model 'Favorite'
        db.create_table(u'bot_favorite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Query'])),
            ('tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Tweet'])),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Campaign'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bot', ['Favorite'])

        # Adding model 'Follower'
        db.create_table(u'bot_follower', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('twitterUserId', self.gf('django.db.models.fields.BigIntegerField')()),
            ('favorite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Favorite'], blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'bot', ['Follower'])


    def backwards(self, orm):
        # Deleting model 'Grammar'
        db.delete_table(u'bot_grammar')

        # Deleting model 'Keyword'
        db.delete_table(u'bot_keyword')

        # Deleting model 'Query'
        db.delete_table(u'bot_query')

        # Removing M2M table for field keywords on 'Query'
        db.delete_table(db.shorten_name(u'bot_query_keywords'))

        # Deleting model 'Campaign'
        db.delete_table(u'bot_campaign')

        # Deleting model 'Tweet'
        db.delete_table(u'bot_tweet')

        # Removing M2M table for field keywords on 'Tweet'
        db.delete_table(db.shorten_name(u'bot_tweet_keywords'))

        # Deleting model 'Favorite'
        db.delete_table(u'bot_favorite')

        # Deleting model 'Follower'
        db.delete_table(u'bot_follower')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bot.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'cycle': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'bot.favorite': {
            'Meta': {'object_name': 'Favorite'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Campaign']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Query']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Tweet']"})
        },
        u'bot.follower': {
            'Meta': {'object_name': 'Follower'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Favorite']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitterUserId': ('django.db.models.fields.BigIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'bot.grammar': {
            'Meta': {'object_name': 'Grammar'},
            'grammar': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bot.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'grammar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Grammar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'bot.query': {
            'Meta': {'object_name': 'Query'},
            'bid': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '9', 'decimal_places': '2'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bot.Keyword']", 'symmetrical': 'False'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'bot.tweet': {
            'Meta': {'object_name': 'Tweet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bot.Keyword']", 'symmetrical': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tweetId': ('django.db.models.fields.BigIntegerField', [], {}),
            'twitterUserId': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['bot']