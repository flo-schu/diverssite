# Generated by Django 3.0.3 on 2020-02-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='category',
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(to='wiki.Category'),
        ),
    ]
