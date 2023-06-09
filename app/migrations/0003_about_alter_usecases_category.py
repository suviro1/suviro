# Generated by Django 4.1.7 on 2023-03-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company_alter_usecases_category_productcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usecases',
            name='category',
            field=models.CharField(choices=[('facility_management', 'Facility_management'), ('water_treatment', 'Water_treatment'), ('electronics_industry', 'Electronics_industry'), ('food', 'Food'), ('precision_machine', 'Precision_machine'), ('oem', 'Oem'), ('smart_Farm', 'Smart_Farm'), ('pharmaceutical_Bio', 'Pharmaceutical_Bio')], max_length=50),
        ),
    ]
