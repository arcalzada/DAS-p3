# Generated by Django 5.1.7 on 2025-03-22 12:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_creationdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='closingDate',
            new_name='closing_date',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='creationDate',
        ),
        migrations.AddField(
            model_name='auction',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
