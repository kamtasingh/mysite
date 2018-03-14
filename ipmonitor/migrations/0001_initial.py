# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type', models.IntegerField(choices=[(1, 'Windows PC'), (2, 'Ubuntu')], default=1)),
                ('operating_system', models.IntegerField(choices=[(1, 'Windows 10 Aniversary'), (2, 'Windows 10 Pro'), (3, 'Windows 10'), (4, 'Windows 8'), (5, 'Windows 7'), (6, 'Ubuntu')], default=1)),
                ('v4_ip', models.GenericIPAddressField(protocol='ipv4')),
                ('hostName', models.CharField(max_length=100, unique=True)),
                ('ram', models.IntegerField(blank=True, null=True)),
                ('symantic', models.BooleanField(default=False)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('cabinet_esxi', models.CharField(blank=True, max_length=100, null=True)),
                ('esxi_server_id', models.CharField(blank=True, max_length=100, null=True)),
                ('softwares', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('owner_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('owner_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
