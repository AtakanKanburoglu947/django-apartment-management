# Generated by Django 4.1.4 on 2022-12-17 01:51

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_payment_month_alter_payment_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(default='content_images/blog_image.png', upload_to='content_images'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 4, 51, 43, 904739)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='year',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 4, 51, 43, 904739)),
        ),
    ]
