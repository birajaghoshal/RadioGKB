# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Submit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='kb',
            field=models.CharField(choices=[('SNP', 'SNP'), ('Exp', 'Expression')], max_length=20),
        ),
    ]