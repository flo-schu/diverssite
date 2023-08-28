# Generated by Django 3.0.3 on 2020-03-23 19:55

from django.db import migrations, models

import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20200322_1927"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="picture",
            field=models.ImageField(null=True, upload_to=users.models.user_profile_directory_path),
        ),
    ]
