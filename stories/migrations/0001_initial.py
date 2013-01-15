# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoryArc'
        db.create_table('stories_storyarc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stories', ['StoryArc'])

        # Adding model 'StoryArcIssue'
        db.create_table('stories_storyarcissue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storyarc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.StoryArc'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Comic'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('stories', ['StoryArcIssue'])


    def backwards(self, orm):
        # Deleting model 'StoryArc'
        db.delete_table('stories_storyarc')

        # Deleting model 'StoryArcIssue'
        db.delete_table('stories_storyarcissue')


    models = {
        'issues.comic': {
            'Meta': {'object_name': 'Comic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.FloatField', [], {}),
            'own': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Series']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'issues.series': {
            'Meta': {'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marvel_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mini_series_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'new52_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'series_max': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'stories.storyarc': {
            'Meta': {'object_name': 'StoryArc'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'stories.storyarcissue': {
            'Meta': {'object_name': 'StoryArcIssue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Comic']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'storyarc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stories.StoryArc']"})
        }
    }

    complete_apps = ['stories']