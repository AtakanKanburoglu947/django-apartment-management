# Generated by Django 4.1.4 on 2022-12-16 13:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_image_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
