# Generated by Django 3.0.5 on 2020-10-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_collectorprofile_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectorprofile',
            name='person_photo',
            field=models.FileField(blank=True, null=True, upload_to='delivery boy photo/'),
        ),
    ]
