# Generated by Django 4.1.4 on 2022-12-16 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_payment_month_alter_payment_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 23, 38, 51, 322737)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='year',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 23, 38, 51, 322737)),
        ),
    ]
