# Generated by Django 3.0.7 on 2020-07-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200722_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='trikotnummer',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
    ]