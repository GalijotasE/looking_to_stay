# Generated by Django 4.1.3 on 2022-12-09 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('looking_to_stay_app', '0007_reservation_status_delete_reservationstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='looking_to_stay_app.hotel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
