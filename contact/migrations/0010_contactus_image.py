# Generated by Django 5.1.7 on 2025-04-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_remove_contactus_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
