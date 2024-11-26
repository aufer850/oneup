# Generated by Django 5.1.3 on 2024-11-23 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_articles_likes_remove_articles_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='articlekey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.articles'),
        ),
        migrations.CreateModel(
            name='ArticleReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.GenericIPAddressField(verbose_name='IP - адреса')),
                ('is_like', models.BooleanField(blank=True, null=True, verbose_name='Лайк')),
                ('articlekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='news.articles')),
            ],
        ),
    ]