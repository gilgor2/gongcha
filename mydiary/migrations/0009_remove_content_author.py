# Generated by Django 3.2.4 on 2021-07-01 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0008_auto_20210701_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='author',
        ),
    ]