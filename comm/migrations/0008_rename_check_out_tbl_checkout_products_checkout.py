# Generated by Django 5.1.1 on 2024-10-23 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0007_remove_tbl_checkout_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_checkout_products',
            old_name='check_out',
            new_name='checkout',
        ),
    ]
