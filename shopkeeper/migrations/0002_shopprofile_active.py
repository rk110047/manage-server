# Generated by Django 2.1.5 on 2020-05-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
