# Generated by Django 3.2.7 on 2021-11-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20211110_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description_author_ar',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description_author_en',
        ),
    ]
