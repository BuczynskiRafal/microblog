# Generated by Django 3.2.9 on 2022-01-26 10:21

import common.models
from django.db import migrations, models
import django.db.models.deletion
import galleries.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tytuł')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'new'), (2, 'hide'), (3, 'published')], default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.models.CheckAgeMixin),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('slug', models.SlugField()),
                ('short_description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Któryki opis')),
                ('image', models.ImageField(upload_to=galleries.models.upload_to)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowano')),
                ('source', models.CharField(blank=True, max_length=512, null=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'new'), (2, 'hide'), (3, 'published')], default=1)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='galleries.gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.models.CheckAgeMixin),
        ),
    ]
