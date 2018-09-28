# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(max_length=35, unique_for_month='pub_date', help_text='A label for URL config')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date publised', auto_now_add=True)),
                ('startups', models.ManyToManyField(db_constraint='blog_posts', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'blog post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
