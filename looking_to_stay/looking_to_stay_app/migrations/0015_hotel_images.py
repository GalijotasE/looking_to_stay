# Generated by Django 4.1.3 on 2022-12-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('looking_to_stay_app', '0014_remove_image_hotel_image_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='images',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='looking_to_stay_app.image'),
        ),
    ]
