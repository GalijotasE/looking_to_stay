# Generated by Django 4.1.3 on 2022-12-01 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('looking_to_stay_app', '0003_city_company_country_alter_category_options_hotel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ['hotel_name'], 'verbose_name': 'Hotel', 'verbose_name_plural': 'Hotels'},
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='company_id',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]