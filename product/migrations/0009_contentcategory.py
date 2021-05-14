# Generated by Django 3.0.5 on 2020-09-05 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120)),
                ('requried', models.IntegerField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('content', models.ManyToManyField(to='product.Content')),
            ],
        ),
    ]
