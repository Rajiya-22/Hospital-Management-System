# Generated by Django 4.2.1 on 2023-09-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0010_alter_patients_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='app_date',
            field=models.DateField(default='2023-09-13'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='description',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
    ]