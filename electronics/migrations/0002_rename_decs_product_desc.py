# Generated by Django 5.1.6 on 2025-02-20 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decs',
            new_name='desc',
        ),
    ]
