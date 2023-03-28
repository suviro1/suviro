# Generated by Django 4.1.7 on 2023-03-26 10:18

import cloudinary.models
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.TextField(max_length=500)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('signal_conversion', 'signal_conversion'), ('environmental_monitoring', 'environmental_monitoring'), ('network', 'network'), ('Temperature_monitoring', 'Temperature_monitoring')], max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('product_img1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('product_img2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('product_img3', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('product_img4', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('moredetails', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Usecases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('precision_machine', 'Precision_machine'), ('facility_management', 'Facility_management'), ('water_treatment', 'Water_treatment'), ('pharmaceutical_Bio', 'Pharmaceutical_Bio'), ('electronics_industry', 'Electronics_industry'), ('food', 'Food'), ('oem', 'Oem'), ('smart_Farm', 'Smart_Farm')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
            ],
        ),
    ]