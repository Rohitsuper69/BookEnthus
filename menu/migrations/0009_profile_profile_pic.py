# Generated by Django 4.2.2 on 2023-07-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_remove_profile_mob_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
