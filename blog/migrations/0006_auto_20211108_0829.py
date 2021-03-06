# Generated by Django 3.2.7 on 2021-11-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211108_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags_ar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.posttag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.posttag'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
