# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nombre',
            new_name='Director',
        ),
        migrations.AddField(
            model_name='post',
            name='FechaPublicacionPelicula',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
