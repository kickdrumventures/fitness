# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Set.quantity'
        db.delete_column(u'workouts_set', 'quantity')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Set.quantity'
        raise RuntimeError("Cannot reverse this migration. 'Set.quantity' and its values cannot be restored.")

    models = {
        u'workouts.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description_long': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'description_short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'exercise_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['workouts.ExerciseType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'workouts.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'workouts.location': {
            'Meta': {'object_name': 'Location'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'workouts.session': {
            'Meta': {'object_name': 'Session'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Location']"})
        },
        u'workouts.set': {
            'Meta': {'object_name': 'Set'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['workouts.Exercise']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reps_mins': ('django.db.models.fields.IntegerField', [], {}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Session']"}),
            'weight_resistance': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['workouts']