# Generated by Django 3.0.5 on 2020-08-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_order_order_preparation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('GENERATED', 'generated'), ('ORDER READY', 'order ready'), ('ACCEPTED BY SHOP', 'acceped by shop'), ('OUT FOR DELIVERY', 'out for delivery'), ('SHIPPED', 'shipped'), ('REFUNDED', 'refunded'), ('CANCELLED', 'cancelled')], default='generated', max_length=120),
        ),
    ]
