# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_stores_from_sql():
    from wedin.settings import BASE_DIR
    import os
    sql_statements = open(os.path.join(BASE_DIR,'wed/sql/wedin_db.sql'), 'r').read()
    return sql_statements


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pix',
            field=models.ImageField(null=True, upload_to=b'pix/', blank=True),
        ),
        migrations.RunSQL(load_stores_from_sql()),
    ]