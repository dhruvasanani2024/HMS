# Generated by Django 5.1.7 on 2025-04-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_data',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
