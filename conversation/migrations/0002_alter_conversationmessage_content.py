# Generated by Django 5.1.5 on 2025-02-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='content',
            field=models.TextField(),
        ),
    ]
