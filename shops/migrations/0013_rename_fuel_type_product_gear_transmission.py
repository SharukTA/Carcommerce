# Generated by Django 5.1 on 2024-09-03 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0012_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='fuel_type',
            new_name='gear_transmission',
        ),
    ]
