# Generated by Django 3.0.5 on 2020-09-24 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('person_photo', models.FileField(upload_to='delivery boy photo/')),
                ('contact_number', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
