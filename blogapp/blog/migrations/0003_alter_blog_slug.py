# Generated by Django 4.1.2 on 2022-10-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
