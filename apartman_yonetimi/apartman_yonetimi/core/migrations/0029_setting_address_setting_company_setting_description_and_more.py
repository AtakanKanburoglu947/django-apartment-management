# Generated by Django 4.1.4 on 2022-12-17 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_setting_alter_content_image_alter_payment_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='address',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='company',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='facebook',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='fax',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='instagram',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='keywords',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='twitter',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 4, 56, 14, 139324)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='year',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 4, 56, 14, 139324)),
        ),
    ]
