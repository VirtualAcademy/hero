# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0002_auto_20160312_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(default=b'', help_text=b'Specific details of this item, such as preferred model.', verbose_name=b'description', blank=True)),
                ('url', models.URLField(default=b'', help_text=b'A website showing the item.', blank=True)),
                ('image', models.ImageField(help_text=b'A photo or illustration.', null=True, upload_to=b'gift_registry/images', blank=True)),
                ('one_only', models.BooleanField(default=True, help_text=b'When checked, remove item from list someone has chosen it. For some items, you may be happy to receive multiple.')),
                ('live', models.BooleanField(default=False, help_text=b'Make this item visible to public.')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Giver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('gift', models.ForeignKey(to='wed.Gift')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='giver',
            unique_together=set([('gift', 'email')]),
        ),
    ]
