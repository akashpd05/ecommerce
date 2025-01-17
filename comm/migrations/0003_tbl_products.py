# Generated by Django 5.1.1 on 2024-09-26 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0002_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('grams', models.CharField(max_length=100)),
                ('pieces', models.CharField(max_length=100)),
                ('serves', models.CharField(max_length=100)),
                ('market_price', models.FloatField()),
                ('our_price', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comm.tbl_subcategory')),
            ],
        ),
    ]
