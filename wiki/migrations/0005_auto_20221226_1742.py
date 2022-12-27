# Generated by Django 3.1.12 on 2022-12-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0004_auto_20221226_1524"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="article",
        ),
        migrations.RemoveField(
            model_name="image",
            name="article",
        ),
        migrations.AddField(
            model_name="article",
            name="files",
            field=models.ManyToManyField(blank=True, default=None, to="wiki.File"),
        ),
        migrations.AddField(
            model_name="article",
            name="images",
            field=models.ManyToManyField(blank=True, default=None, to="wiki.Image"),
        ),
    ]