# Generated by Django 5.1.3 on 2024-11-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0005_alter_profile_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='upload',
            field=models.ImageField(blank=True, default='static/img/default-pfp.jpg', upload_to='images/'),
        ),
    ]
