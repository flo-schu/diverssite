# Generated by Django 3.0.7 on 2020-11-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("public", "0008_delete_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Info",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("welcome_title", models.TextField(blank=True, null=True)),
                ("welcome_text", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
