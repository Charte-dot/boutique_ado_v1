# Generated by Django 3.2 on 2022-10-01 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221001_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_size',
            new_name='has_sizes',
        ),
    ]
