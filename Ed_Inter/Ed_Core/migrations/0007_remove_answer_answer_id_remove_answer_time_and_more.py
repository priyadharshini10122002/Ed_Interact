# Generated by Django 5.0.3 on 2024-03-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ed_Core', '0006_answer_id_commend_id_reply_id_alter_answer_answer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='time',
        ),
        migrations.RemoveField(
            model_name='commend',
            name='command_id',
        ),
        migrations.RemoveField(
            model_name='commend',
            name='time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='reply_id',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='time',
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='commend',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
