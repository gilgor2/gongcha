# Generated by Django 3.2.4 on 2021-07-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0010_auto_20210701_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='limit',
            field=models.IntegerField(default=0),
        ),
    ]
