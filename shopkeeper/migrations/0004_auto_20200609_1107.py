# Generated by Django 2.1.5 on 2020-06-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0003_shopprofile_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopprofile',
            name='timming',
            field=models.CharField(max_length=120),
        ),
    ]
