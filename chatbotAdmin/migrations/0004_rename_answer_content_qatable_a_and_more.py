# Generated by Django 4.2.7 on 2023-11-20 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotAdmin', '0003_remove_qatable_question_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qatable',
            old_name='answer_content',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='qatable',
            old_name='question_content',
            new_name='q',
        ),
    ]