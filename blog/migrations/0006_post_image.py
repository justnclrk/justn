# Generated by Django 3.0.7 on 2020-08-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200608_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='posts_images'),
        ),
    ]
