# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComicReadAndOwn'
        db.create_table('comicFiles_comicreadandown', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Comic'])),
            ('own', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('read', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('comicFiles', ['ComicReadAndOwn'])


    def backwards(self, orm):
        # Deleting model 'ComicReadAndOwn'
        db.delete_table('comicFiles_comicreadandown')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'comicFiles.comicfile': {
            'Meta': {'unique_together': "(('name', 'dir_path'),)", 'object_name': 'ComicFile'},
            'ads': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'comic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Comic']", 'null': 'True', 'blank': 'True'}),
            'comic_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_issue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comic_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_volume': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dir_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'error_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'review_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rootFolder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comicFiles.RootFolder']", 'null': 'True', 'blank': 'True'}),
            'scan_quallity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'comicFiles.comicreadandown': {
            'Meta': {'object_name': 'ComicReadAndOwn'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Comic']"}),
            'own': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'read': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'comicFiles.primarycomics': {
            'Meta': {'unique_together': "(('series', 'comic', 'comicFile'),)", 'object_name': 'PrimaryComics'},
            'comic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Comic']"}),
            'comicFile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comicFiles.ComicFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Series']"})
        },
        'comicFiles.rootfolder': {
            'Meta': {'object_name': 'RootFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_scanned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'comicFiles.transferroot': {
            'Meta': {'object_name': 'TransferRoot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issues.comic': {
            'Meta': {'object_name': 'Comic'},
            'annual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'annual_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'alt_search_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'front_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marvel_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mini_series_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'new52_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'series_max': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['comicFiles']