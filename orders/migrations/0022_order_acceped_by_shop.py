# Generated by Django 2.1.5 on 2020-07-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_order_order_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='acceped_by_shop',
            field=models.BooleanField(default=False),
        ),
    ]