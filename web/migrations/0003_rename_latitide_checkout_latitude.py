# Generated by Django 4.1.1 on 2023-03-10 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_checkout_delivery_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='latitide',
            new_name='latitude',
        ),
    ]
