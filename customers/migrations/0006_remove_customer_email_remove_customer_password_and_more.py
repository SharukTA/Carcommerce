# Generated by Django 5.1 on 2024-08-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
