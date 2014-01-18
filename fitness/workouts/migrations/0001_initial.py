# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table(u'workouts_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_short', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description_long', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('type_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'workouts', ['Exercise'])

        # Adding model 'ExerciseType'
        db.create_table(u'workouts_exercisetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'workouts', ['ExerciseType'])

        # Adding model 'Location'
        db.create_table(u'workouts_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'workouts', ['Location'])

        # Adding model 'Session'
        db.create_table(u'workouts_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Location'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'workouts', ['Session'])

        # Adding model 'Set'
        db.create_table(u'workouts_set', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Session'])),
            ('exercise_id', self.gf('django.db.models.fields.IntegerField')()),
            ('reps_mins', self.gf('django.db.models.fields.IntegerField')()),
            ('weight_resistance', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'workouts', ['Set'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table(u'workouts_exercise')

        # Deleting model 'ExerciseType'
        db.delete_table(u'workouts_exercisetype')

        # Deleting model 'Location'
        db.delete_table(u'workouts_location')

        # Deleting model 'Session'
        db.delete_table(u'workouts_session')

        # Deleting model 'Set'
        db.delete_table(u'workouts_set')


    models = {
        u'workouts.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description_long': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'description_short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_id': ('django.db.models.fields.IntegerField', [], {})
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
            'exercise_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reps_mins': ('django.db.models.fields.IntegerField', [], {}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Session']"}),
            'weight_resistance': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['workouts']