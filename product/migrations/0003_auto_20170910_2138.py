# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-10 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170910_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Country'),
        ),
        migrations.AlterField(
            model_name='product',
            name='packing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Packing'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Subcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_or_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.TypeOrUser'),
        ),
    ]
