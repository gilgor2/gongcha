# Generated by Django 3.2.4 on 2021-07-01 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mydiary', '0006_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_posts', models.ManyToManyField(blank=True, related_name='like_users', to='mydiary.Content')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mydiary.profile'),
        ),
    ]
