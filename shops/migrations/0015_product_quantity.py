# Generated by Django 5.1 on 2024-09-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0014_alter_product_gear_transmission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
