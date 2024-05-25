# Generated by Django 4.2.1 on 2023-10-05 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0034_delete_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default='Cardiologist', max_length=70, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HospitalManagement.departments'),
        ),
    ]