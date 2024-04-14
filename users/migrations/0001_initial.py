# Generated by Django 3.0.3 on 2020-03-15 10:57

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
            name="Profile",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("firstname", models.CharField(max_length=50, null=True)),
                ("lastname", models.CharField(max_length=50, null=True)),
                ("gender", models.CharField(choices=[("d", "divers"), ("f", "female"), ("m", "male")], max_length=10)),
                ("trikotnummer", models.CharField(max_length=3, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("street", models.CharField(max_length=50, null=True)),
                ("place", models.CharField(max_length=50, null=True)),
                ("zip", models.CharField(max_length=50, null=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
