# Generated by Django 4.0 on 2022-07-12 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_appointment_orders_appointment_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='order',
            new_name='orders',
        ),
    ]
