# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('means', models.CharField(max_length=200)),
                ('direction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtitle', models.CharField(max_length=20)),
                ('intro', models.TextField()),
                ('startime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
                ('pix', models.ImageField(null=True, upload_to=b'/pix', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('event', models.ForeignKey(to='wed.Event')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'gallery/')),
                ('alt_text', models.CharField(default=b'pic', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Giftregistry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField()),
                ('signature', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Gift Registries',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groom_nick', models.CharField(max_length=10)),
                ('bride_nick', models.CharField(max_length=10)),
                ('slogan', models.CharField(max_length=100)),
                ('wedin_date', models.DateField()),
                ('email', models.EmailField(default=b'odieleowedding@gmail.com', max_length=254)),
                ('phone', models.CharField(default=b'00237677757776', max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Heroes',
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('guests', models.PositiveSmallIntegerField()),
                ('attending', models.BooleanField()),
                ('events', models.CharField(max_length=200)),
                ('guestinfo', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.AddField(
            model_name='direction',
            name='event',
            field=models.ForeignKey(to='wed.Event'),
        ),
    ]
