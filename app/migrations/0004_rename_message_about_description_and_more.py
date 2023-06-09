# Generated by Django 4.1.7 on 2023-03-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about_alter_usecases_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='message',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='usecases',
            name='category',
            field=models.CharField(choices=[('oem', 'Oem'), ('precision_machine', 'Precision_machine'), ('water_treatment', 'Water_treatment'), ('food', 'Food'), ('smart_Farm', 'Smart_Farm'), ('pharmaceutical_Bio', 'Pharmaceutical_Bio'), ('electronics_industry', 'Electronics_industry'), ('facility_management', 'Facility_management')], max_length=50),
        ),
    ]
