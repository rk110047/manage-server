# Generated by Django 2.1.5 on 2020-07-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_remove_address_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='alternate_phone_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='landmark',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
