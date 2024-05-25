# Generated by Django 4.2.1 on 2023-09-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('doctor_id', models.IntegerField(default=5000, primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='null', max_length=40)),
                ('lastname', models.CharField(default='null', max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.CharField(default='null', max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]