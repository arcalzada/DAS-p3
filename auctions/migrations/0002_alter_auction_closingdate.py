# Generated by Django 5.1.7 on 2025-03-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='closingDate',
            field=models.DateTimeField(),
        ),
    ]
