# Generated by Django 5.1.3 on 2024-11-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0004_remove_profile_image_profile_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='upload',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
