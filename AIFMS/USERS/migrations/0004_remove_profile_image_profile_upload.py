# Generated by Django 5.1.3 on 2024-11-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0003_remove_profile_theme_name_remove_profile_theme_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='upload',
            field=models.ImageField(default='images/default-pfp.jpg', upload_to='images/'),
        ),
    ]