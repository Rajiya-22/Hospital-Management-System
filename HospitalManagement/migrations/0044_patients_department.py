# Generated by Django 4.2.1 on 2023-10-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0043_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HospitalManagement.departments'),
        ),
    ]
