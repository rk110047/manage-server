# Generated by Django 3.0.5 on 2020-10-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20200917_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Aisle_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Shelf_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Shelf_side',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
