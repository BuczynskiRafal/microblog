# Generated by Django 3.2.9 on 2021-12-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_user_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts/examples/'),
        ),
    ]