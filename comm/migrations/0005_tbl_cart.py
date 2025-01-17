# Generated by Django 5.1.1 on 2024-10-04 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0004_tbl_sign_up_tbl_buy_now'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('session_key', models.CharField(max_length=100)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comm.tbl_products')),
            ],
        ),
    ]
