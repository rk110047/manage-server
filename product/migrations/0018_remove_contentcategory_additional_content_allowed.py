# Generated by Django 3.0.5 on 2020-09-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20200915_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentcategory',
            name='additional_content_allowed',
        ),
    ]