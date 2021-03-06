# Generated by Django 2.2 on 2020-08-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200806_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='update',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
