# Generated by Django 5.0.3 on 2024-03-21 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ed_Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ed_Core.login_info'),
        ),
    ]
