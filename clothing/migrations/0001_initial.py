# Generated by Django 5.1.6 on 2025-02-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large')], default='M', max_length=3)),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White'), ('Brown', 'Brown')], default='Black', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_img/')),
            ],
        ),
    ]
