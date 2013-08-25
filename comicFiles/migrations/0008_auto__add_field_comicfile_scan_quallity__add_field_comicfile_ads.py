# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ComicFile.scan_quallity'
        db.add_column('comicFiles_comicfile', 'scan_quallity',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ComicFile.ads'
        db.add_column('comicFiles_comicfile', 'ads',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ComicFile.scan_quallity'
        db.delete_column('comicFiles_comicfile', 'scan_quallity')

        # Deleting field 'ComicFile.ads'
        db.delete_column('comicFiles_comicfile', 'ads')


    models = {
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
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['comicFiles']