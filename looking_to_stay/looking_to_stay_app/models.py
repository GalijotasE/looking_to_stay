from django.db import models
from django.utils.html import format_html
from django.urls import reverse


class Country(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    country_name = models.CharField('Country', max_length=50, help_text='Enter a name of the country')

    def __str__(self) -> str:
        return self.country_name

    class Meta:
        ordering = ['country_name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    city_name = models.CharField('City', max_length=50, help_text='Please enter a name of the city')
    country_id = models.ForeignKey(
        Country, on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    def __str__(self) -> str:
        return f'{self.city_name} - {self.country_id}'

    class Meta:
        ordering = ['city_name', 'country_id',]
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


# class Company(models.Model):
#     id = models.AutoField('Unique ID', primary_key=True)
#     company_name = models.CharField('Company Name', max_length=128, help_text='Please type a name of the company')
#     email = models.CharField('Email', max_length=128)
#     phone_number = models.CharField('Phone Number', max_length=13)
#     postal_code = models.CharField('Postal Code', max_length=10)
#     address = models.CharField('Address', max_length=255)

#     def __str__(self) -> str:
#         return {self.company_name}

#     class Meta():
#         ordering = ['company_name']
#         verbose_name = 'Company'
#         verbose_name_plural = 'Companies'


class Category(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    category_name = models.CharField('Category', max_length=128, help_text='Please type a name of the category')

    def link_filtered_hotels(self):
        link = reverse('hotels')+'?category_id='+str(self.id)
        return format_html('<a class="category" href="{link}">{name}</a>', link=link, name=self.category_name)
    

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Currency(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    currency = models.CharField('Currency', max_length=3, help_text='Currency name consisting of 3 letters, eg:EUR/USD/GBP')

    def __str__(self) -> str:
        return self.currency

    class Meta:
        ordering = ['currency',]
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Hotel(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    hotel_name = models.CharField('Hotel Name', max_length=100, help_text="Please enter a name of the Hotel")
    description = models.TextField('Description', max_length=10000,
        help_text='Please enter a description of the hotel, consisting up to 10000 words.')
    # company_id = models.ForeignKey(
    #     Company, on_delete=models.SET_NULL,
    #     null=True, blank=True,
    # )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    price_from = models.IntegerField('Price per night from')
    type_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    cover_photo = models.ImageField('Cover Photo', upload_to='covers', blank=True, null=True, )

    def __str__(self) -> str:
        return self.hotel_name

    class Meta:
        ordering = ['hotel_name',]
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'



class RoomType(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    name = models.CharField('Type Name', max_length=255, help_text='Name of the room type')
    price = models.IntegerField('Price Per Night', help_text='Please enter the price for the night')
    currency_type = models.ForeignKey(
        Currency, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    people = models.IntegerField('People', help_text='Amount of people fit in this room')
    
    def __str__(self) -> str:
        return f'{self.name} - {self.price} a night'

    class Meta:
        ordering = ['price',]


class Amenities(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    amenity = models.CharField('Amenity', max_length=255, help_text='Please enter amenities provided')

    def __str__(self) -> str:
        return self.amenity

    class Meta:
        ordering = ['amenity',]
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class Room(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    room_name = models.CharField('Room name', max_length=255)
    room_type_id = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    amenities = models.ManyToManyField(
        Amenities, help_text='Choose amenities of this room',
        verbose_name='amenities'
    )
    hotel_id = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.room_name

    class Meta:
        ordering = ['room_name',]

class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.FileField(upload_to='images/')

    def __str__(self) -> str:
        return self.hotel.hotel_name



# class Reviews(models.Model):
#     pass


# class RoomReserved(models.Model):
#     pass


# class Reservation(models.Model):
#     pass


# class ReservationStatus(models.Model):
#     pass


# class User(models.Model):
#     pass