# Generated by Django 4.1.3 on 2022-12-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('looking_to_stay_app', '0006_reservationstatus_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Drafted'), ('u', 'Unoccupied'), ('r', 'Reserved'), ('o', 'Occupied')], default='u', help_text='Reservation Status', max_length=1),
        ),
        migrations.DeleteModel(
            name='ReservationStatus',
        ),
    ]
