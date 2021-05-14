# Generated by Django 2.1.5 on 2020-07-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200712_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('CREATED', 'created'), ('ACCEPTED BY SHOP', 'acceped by shop'), ('OUT FOR DELIVERY', 'out for delivery'), ('SHIPPED', 'shipped'), ('REFUNDED', 'refunded'), ('CANCELLED', 'cancelled')], default='created', max_length=120),
        ),
    ]