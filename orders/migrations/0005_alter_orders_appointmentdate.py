# Generated by Django 4.0 on 2022-07-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orders_appointmentdate_orders_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='appointmentdate',
            field=models.DateField(blank=True, verbose_name='Randevu Tarihi'),
        ),
    ]