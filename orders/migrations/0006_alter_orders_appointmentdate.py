# Generated by Django 4.0 on 2022-07-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orders_appointmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='appointmentdate',
            field=models.DateField(blank=True, null=True, verbose_name='Randevu Tarihi'),
        ),
    ]
