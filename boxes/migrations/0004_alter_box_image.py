# Generated by Django 3.2 on 2022-04-17 08:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0003_remove_box_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]