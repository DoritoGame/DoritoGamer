# Generated by Django 5.0.2 on 2024-03-11 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_user_ident_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 11, 5, 51, 95745)),
        ),
    ]
