# Generated by Django 3.0.7 on 2021-02-14 13:51

import markdownx.models
from django.db import migrations, models

import wiki.models


class Migration(migrations.Migration):

    replaces = [
        ("wiki", "0001_initial"),
        ("wiki", "0002_auto_20200228_2124"),
        ("wiki", "0003_articles_slug"),
        ("wiki", "0004_articles_pub_date"),
        ("wiki", "0005_auto_20200229_1715"),
        ("wiki", "0006_auto_20200303_2118"),
        ("wiki", "0007_auto_20200807_0031"),
        ("wiki", "0008_auto_20200807_0052"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Display",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("text", markdownx.models.MarkdownxField()),
                ("pub_date", models.DateField(auto_now_add=True)),
                ("slug", models.SlugField()),
                (
                    "visibility",
                    models.CharField(
                        choices=[("public", "Public"), ("members", "Members")],
                        default="public",
                        max_length=20,
                    ),
                ),
                ("category", models.ManyToManyField(to="wiki.Category")),
                ("show_on_pages", models.ManyToManyField(to="wiki.Display")),
            ],
        ),
        migrations.CreateModel(
            name="Files",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to=wiki.models.file_directory_path, verbose_name="File"),
                ),
                ("article", models.ManyToManyField(default=None, to="wiki.Article")),
            ],
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=wiki.models.file_directory_path, verbose_name="Image"),
                ),
                ("article", models.ManyToManyField(default=None, to="wiki.Article")),
            ],
        ),
    ]
