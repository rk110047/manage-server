# Generated by Django 2.1.5 on 2020-07-12 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_delivery_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryPersonProfile'),
        ),
    ]