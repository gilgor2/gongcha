# Generated by Django 3.2.4 on 2021-07-01 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0005_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
