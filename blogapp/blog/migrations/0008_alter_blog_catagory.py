# Generated by Django 4.1.2 on 2022-10-08 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.catagory'),
        ),
    ]
