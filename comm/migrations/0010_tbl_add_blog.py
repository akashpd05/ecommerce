# Generated by Django 5.1.1 on 2024-11-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0009_tbl_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_add_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_content', models.CharField(max_length=100)),
            ],
        ),
    ]
