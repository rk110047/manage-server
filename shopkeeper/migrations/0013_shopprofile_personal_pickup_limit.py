# Generated by Django 3.0.5 on 2020-10-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0012_auto_20201004_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='personal_pickup_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
