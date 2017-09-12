# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-10 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import vendor.items.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=23, verbose_name='Packing text')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOrUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_or_user', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='SKU',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='manifacturere',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=vendor.items.fields.ThumbnailImageField(blank=True, null=True, storage=vendor.items.fields.MyFileSystemStorage(), upload_to='products_photo/'),
        ),
        migrations.AddField(
            model_name='product',
            name='retail_unit_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='size_weight',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='zero_gst',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description (optional)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Name of the Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='packing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Packing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='type_or_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.TypeOrUser'),
            preserve_default=False,
        ),
    ]
