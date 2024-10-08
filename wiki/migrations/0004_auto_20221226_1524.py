# Generated by Django 3.1.12 on 2022-12-26 14:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0003_auto_20221226_1443"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="date",
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="time",
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="title",
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name="image",
            name="date",
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="time",
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="title",
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name="file",
            name="article",
            field=models.ManyToManyField(blank=True, default=None, to="wiki.Article"),
        ),
        migrations.AlterField(
            model_name="image",
            name="article",
            field=models.ManyToManyField(blank=True, default=None, to="wiki.Article"),
        ),
    ]
