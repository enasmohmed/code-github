# Generated by Django 3.2.7 on 2021-11-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_description_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_author',
            field=models.ImageField(default='assets/img/Business-elite-logo-none-bg.png', upload_to='post/', verbose_name='image_author'),
        ),
    ]