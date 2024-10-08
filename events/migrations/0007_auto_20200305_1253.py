# Generated by Django 3.0.3 on 2020-03-05 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0006_auto_20200228_2109"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categ",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="categ",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="events.Categ"),
        ),
    ]
