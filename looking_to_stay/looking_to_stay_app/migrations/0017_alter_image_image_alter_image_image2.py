# Generated by Django 4.1.3 on 2022-12-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('looking_to_stay_app', '0016_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image2',
            field=models.ImageField(upload_to='images/'),
        ),
    ]