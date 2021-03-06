# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-22 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='cost',
        ),
        migrations.AlterField(
            model_name='scheme',
            name='comment',
            field=models.TextField(help_text='Enter a comment.  You can include what has been done and what needs to be doing, such as Building Works have been completed, now needs to comply with Health & Safety Requirements.  Or you can just include feedback with or without further actions, such as Good Work.'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='completion',
            field=models.DecimalField(decimal_places=2, help_text='Enter a percentage, (e.g. 25 for Partially Complete or 100 for Complete)', max_digits=3),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='description',
            field=models.TextField(help_text='Enter description of scheme (e.g. The Ely Southern Bypass is designed to Reduce Bridge Strikes).'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='title',
            field=models.CharField(help_text='Enter scheme title (e.g. Ely Southern Bypass, Garden Lighting).', max_length=100),
        ),
    ]
