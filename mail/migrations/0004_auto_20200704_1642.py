# Generated by Django 3.0.7 on 2020-07-04 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mail", "0003_auto_20200704_1612"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="sent",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="message",
            name="recipients",
            field=models.ManyToManyField(related_name="message_recipients_set", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="message",
            name="sender",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="message_sender_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
