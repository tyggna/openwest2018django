# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeInv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('desc', models.TextField()),
                ('model_name', models.CharField(max_length=40)),
            ],
        ),
    ]