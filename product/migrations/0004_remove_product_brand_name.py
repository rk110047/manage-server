# Generated by Django 2.1.5 on 2020-06-15 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_product_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_name',
        ),
    ]
