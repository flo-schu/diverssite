# Generated by Django 3.0.7 on 2020-06-14 21:28
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('events', '0008_auto_20200305_1304'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
    ]