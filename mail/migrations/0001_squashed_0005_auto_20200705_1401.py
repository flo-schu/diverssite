# Generated by Django 3.0.7 on 2021-02-14 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('mail', '0001_initial'), ('mail', '0002_auto_20200704_1610'), ('mail', '0003_auto_20200704_1612'), ('mail', '0004_auto_20200704_1642'), ('mail', '0005_auto_20200705_1401')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(upload_to='')),
                ('recipients', models.ManyToManyField(related_name='message_recipients_set', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='message_sender_set', to=settings.AUTH_USER_MODEL)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
