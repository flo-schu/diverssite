# Generated by Django 3.0.3 on 2020-02-15 23:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("training", "Training"),
                            ("tournament", "Tournament"),
                            ("social", "Social Event"),
                            ("orga", "Organization Event"),
                            ("other", "Other"),
                        ],
                        default="Training",
                        max_length=20,
                    ),
                ),
                ("date", models.DateTimeField()),
                ("description", models.TextField(null=True)),
                ("visibility", models.CharField(default="public", max_length=20)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=100)),
                ("place", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Participation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "participation",
                    models.CharField(choices=[("y", "Yes"), ("n", "No"), ("m", "Maybe")], default="n", max_length=10),
                ),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="events.Event")),
                ("person", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="events.Location"),
        ),
    ]
