# Generated by Django 3.0.7 on 2020-06-08 06:44

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_sum_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sum_content',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
