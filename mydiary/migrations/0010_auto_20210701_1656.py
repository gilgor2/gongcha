# Generated by Django 3.2.4 on 2021-07-01 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0009_remove_content_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='profile',
        ),
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_content', to='mydiary.profile'),
        ),
        migrations.AddField(
            model_name='content',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_users_content', to='mydiary.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_posts_profile', to='mydiary.Content'),
        ),
    ]