# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-22 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='scheme',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, help_text='Enter name of country (e.g. United Kingdom)', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, help_text='Enter name of county (e.g. Cambs or Cambridgeshire).  This field is optional.', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(help_text='Enter full name of individual (e.g. Joe Bloggs) or Business (e.g. Facebook)', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number (can be landline or mobile)', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, help_text='Enter postcode (e.g. BR1 3ES)', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(help_text='Enter first line of home or business address', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, help_text='Enter second line of home or business address (optional)', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(help_text='Enter name of town or city (e.g. March, Peterborough)', max_length=40),
        ),
    ]