# Generated by Django 3.0.7 on 2021-07-24 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_assist', to=settings.AUTH_USER_MODEL)),
                ('hockey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_hockey', to=settings.AUTH_USER_MODEL)),
                ('score', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_score', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_team', to='ultistats.Team')),
            ],
        ),
    ]
