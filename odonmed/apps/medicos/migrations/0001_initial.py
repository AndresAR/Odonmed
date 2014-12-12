# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Medico'
        db.create_table(u'medicos_medico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'medicos', ['Medico'])

        # Adding M2M table for field dias on 'Medico'
        m2m_table_name = db.shorten_name(u'medicos_medico_dias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medico', models.ForeignKey(orm[u'medicos.medico'], null=False)),
            ('hora', models.ForeignKey(orm[u'horas.hora'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medico_id', 'hora_id'])

        # Adding model 'HoraMedico'
        db.create_table(u'medicos_horamedico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medicos.Medico'], unique=True)),
            ('hora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horas.Hora'], unique=True)),
            ('tomada', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'medicos', ['HoraMedico'])


    def backwards(self, orm):
        # Deleting model 'Medico'
        db.delete_table(u'medicos_medico')

        # Removing M2M table for field dias on 'Medico'
        db.delete_table(db.shorten_name(u'medicos_medico_dias'))

        # Deleting model 'HoraMedico'
        db.delete_table(u'medicos_horamedico')


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
        u'auth.user': {
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
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'horas.hora': {
            'Meta': {'object_name': 'Hora'},
            'dias': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'medicos.horamedico': {
            'Meta': {'object_name': 'HoraMedico'},
            'hora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horas.Hora']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicos.Medico']", 'unique': 'True'}),
            'tomada': ('django.db.models.fields.BooleanField', [], {})
        },
        u'medicos.medico': {
            'Meta': {'object_name': 'Medico'},
            'dias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['horas.Hora']", 'symmetrical': 'False'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['medicos']