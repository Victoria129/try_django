# Generated by Django 2.2 on 2020-08-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
