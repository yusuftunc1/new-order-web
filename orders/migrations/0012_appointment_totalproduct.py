# Generated by Django 4.0 on 2022-07-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_rename_order_appointment_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='totalproduct',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]