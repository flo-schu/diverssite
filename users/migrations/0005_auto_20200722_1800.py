# Generated by Django 3.0.7 on 2020-07-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_auto_20200719_1603"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="trikotnummer",
            field=models.CharField(
                blank=True,
                error_messages={"unique": "this number is already occupied"},
                max_length=3,
                null=True,
                unique=True,
            ),
        ),
    ]
