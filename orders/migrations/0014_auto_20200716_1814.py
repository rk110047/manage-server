# Generated by Django 2.1.5 on 2020-07-16 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0013_order_shipped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='User',
        ),
        migrations.AddField(
            model_name='order',
            name='User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
