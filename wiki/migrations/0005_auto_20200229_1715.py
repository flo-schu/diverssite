# Generated by Django 3.0.3 on 2020-02-29 16:15

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_articles_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
