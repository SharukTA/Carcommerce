# Generated by Django 5.1 on 2024-08-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0009_shopowner_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopowner',
            name='reject',
            field=models.BooleanField(default=False),
        ),
    ]
