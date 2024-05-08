# Generated by Django 5.0.2 on 2024-05-08 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_articlecategory_articles_and_more'),
        ('user_management', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.ImageField(null=True, upload_to='article_headers/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='user_management.profile')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
