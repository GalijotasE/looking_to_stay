# Generated by Django 4.1.3 on 2022-12-08 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('looking_to_stay_app', '0005_alter_reservationstatus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationstatus',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
