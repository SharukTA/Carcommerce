# Generated by Django 5.1 on 2024-08-21 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shopowner_is_rejected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopowner',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='shopowner',
            name='is_rejected',
        ),
    ]
