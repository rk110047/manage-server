# Generated by Django 3.0.5 on 2020-09-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20200819_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='inFavourite',
            field=models.BooleanField(default=False),
        ),
    ]