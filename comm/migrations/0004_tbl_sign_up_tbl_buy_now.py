# Generated by Django 5.1.1 on 2024-10-01 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0003_tbl_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_buy_now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('town_city', models.CharField(max_length=100)),
                ('state_country', models.CharField(max_length=100)),
                ('zip', models.IntegerField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comm.tbl_products')),
            ],
        ),
    ]