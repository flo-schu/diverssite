# Generated by Django 3.0.2 on 2020-02-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20200207_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(default='public', max_length=20),
        ),
    ]