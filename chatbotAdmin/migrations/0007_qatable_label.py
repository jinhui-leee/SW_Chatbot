# Generated by Django 4.2.7 on 2023-11-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotAdmin', '0006_rename_a_qatable_answer_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qatable',
            name='label',
            field=models.IntegerField(default=0),
        ),
    ]