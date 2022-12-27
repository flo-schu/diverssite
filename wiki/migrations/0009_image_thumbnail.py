# Generated by Django 3.1.12 on 2022-12-27 21:07

from django.db import migrations, models
import wiki.models


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0008_auto_20221226_2300"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="thumbnail",
            field=models.ImageField(
                default="/static/images/default_profile_thumbnail.png",
                upload_to=wiki.models.file_directory_path_tumbnail,
            ),
        ),
    ]