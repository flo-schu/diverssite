# Generated by Django 3.1.12 on 2023-08-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20230826_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
