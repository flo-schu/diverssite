# Generated by Django 3.1.12 on 2022-12-27 22:51

from django.db import migrations, models

import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_squashed_0007_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="thumbnail",
            field=models.ImageField(
                default="/static/images/default_profile_thumbnail.png",
                editable=False,
                upload_to=users.models.file_directory_path_tumbnail,
            ),
        ),
    ]
