# Generated by Django 3.2 on 2022-04-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('years', models.DecimalField(decimal_places=2, max_digits=6)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
