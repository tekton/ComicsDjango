# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RootFolder'
        db.create_table('comicFiles_rootfolder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_scanned', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('comicFiles', ['RootFolder'])

        # Adding model 'ComicFile'
        db.create_table('comicFiles_comicfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dir_path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rootFolder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comicFiles.RootFolder'], null=True, blank=True)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comic_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comic_issue', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comic_volume', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comic_year', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comic_date', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Comic'], null=True, blank=True)),
        ))
        db.send_create_signal('comicFiles', ['ComicFile'])

        # Adding unique constraint on 'ComicFile', fields ['name', 'dir_path']
        db.create_unique('comicFiles_comicfile', ['name', 'dir_path'])


    def backwards(self, orm):
        # Removing unique constraint on 'ComicFile', fields ['name', 'dir_path']
        db.delete_unique('comicFiles_comicfile', ['name', 'dir_path'])

        # Deleting model 'RootFolder'
        db.delete_table('comicFiles_rootfolder')

        # Deleting model 'ComicFile'
        db.delete_table('comicFiles_comicfile')


    models = {
        'comicFiles.comicfile': {
            'Meta': {'unique_together': "(('name', 'dir_path'),)", 'object_name': 'ComicFile'},
            'comic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Comic']", 'null': 'True', 'blank': 'True'}),
            'comic_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_issue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_volume': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comic_year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dir_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'error_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'review_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rootFolder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comicFiles.RootFolder']", 'null': 'True', 'blank': 'True'})
        },
        'comicFiles.rootfolder': {
            'Meta': {'object_name': 'RootFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_scanned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'issues.comic': {
            'Meta': {'object_name': 'Comic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
        }
    }

    complete_apps = ['comicFiles']