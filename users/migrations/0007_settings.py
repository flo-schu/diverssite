# Generated by Django 3.0.7 on 2020-11-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20200722_1910"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "registration_password",
                    models.CharField(help_text="Passwort wird bei der Registrierung abgefragt", max_length=20),
                ),
            ],
        ),
    ]
