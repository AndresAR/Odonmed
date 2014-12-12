# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hora'
        db.create_table(u'horas_hora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dias', self.gf('django.db.models.fields.DateField')()),
            ('horas', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'horas', ['Hora'])


    def backwards(self, orm):
        # Deleting model 'Hora'
        db.delete_table(u'horas_hora')


    models = {
        u'horas.hora': {
            'Meta': {'object_name': 'Hora'},
            'dias': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['horas']