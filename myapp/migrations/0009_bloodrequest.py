# Generated by Django 3.0.5 on 2024-11-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20241125_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_age', models.IntegerField()),
                ('reason', models.TextField()),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('unit', models.IntegerField()),
            ],
        ),
    ]