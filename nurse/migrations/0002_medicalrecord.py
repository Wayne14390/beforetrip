# Generated by Django 5.1.6 on 2025-02-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
                ('visit_date', models.DateField()),
            ],
        ),
    ]
