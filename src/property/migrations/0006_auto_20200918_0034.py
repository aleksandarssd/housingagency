# Generated by Django 3.1.1 on 2020-09-17 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Sale', 'sale'), ('Rent', 'rent')], max_length=50),
        ),
    ]