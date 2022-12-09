from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html
from django.urls import reverse
import uuid
from django.conf import settings
from django.db.models import Avg, Count


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


class HotelImage(models.Model):
    name = models.CharField('name', max_length=255, help_text='Pick any name for this album')
    hotel_img1 = models.ImageField(upload_to='images/', help_text='Choose the main photo')
    hotel_img2 = models.ImageField(upload_to='images/')
    hotel_img3 = models.ImageField(upload_to='images/')
    hotel_img4 = models.ImageField(upload_to='images/')
    hotel_img5 = models.ImageField(upload_to='images/')
    hotel_img6 = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f'{self.name}'



class Amenities(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    amenity = models.CharField('Amenity', max_length=255, help_text='Please enter amenities provided')

    def __str__(self) -> str:
        return self.amenity

    class Meta:
        ordering = ['amenity',]
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class RoomType(models.Model):
    id = models.AutoField('Unique Id', primary_key=True)
    name = models.CharField('Type Name', max_length=255, help_text='Name of the room type')
    price = models.IntegerField('Price Per Night', help_text='Please enter the price for the night')
    currency_type = models.ForeignKey(
        Currency, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    people = models.IntegerField('People', help_text='Amount of people fit in this room')
    total_rooms = models.IntegerField('Rooms', help_text="Total amount of rooms of this type")
    
    def __str__(self) -> str:
        return f'{self.name} - {self.price} a night'

    class Meta:
        ordering = ['price',]


class Hotel(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    hotel_name = models.CharField('Hotel Name', max_length=100, help_text="Please enter a name of the Hotel")
    description = models.TextField('Description', max_length=10000,
        help_text='Please enter a description of the hotel, consisting up to 10000 words.')
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    address = models.CharField('Address', max_length=255, help_text='Address of the hotel')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    price_from = models.IntegerField('Price per night from')
    room_types = models.ManyToManyField(RoomType, help_text="Please select room types")
    type_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    cover_photo = models.ImageField('Cover Photo', upload_to='covers', blank=True, null=True, )
    hotel_images = models.OneToOneField(HotelImage, on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField(
        Amenities, help_text='Choose amenities of this room',
        verbose_name='amenities'
    )

    def averagereview(self):
        review = ReviewRating.objects.filter(single_property=self).aggregate(average=Avg('rating'))
        avg=0
        if review['average'] is not None:
            avg = float(review['average'])
        return avg

    def countreview(self):
        reviews = ReviewRating.objects.filter(single_property=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = int(reviews['count'])
        return cnt

    def listreviews(self):
        reviews = ReviewRating.objects.all()
        return reviews

    def __str__(self) -> str:
        return self.hotel_name

    class Meta:
        ordering = ['hotel_name',]


class Reservation(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='user',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('City', max_length=100)
    post_code = models.CharField('Post code', max_length=10)
    address = models.CharField('Address', max_length=255)
    property = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    roomtype = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    check_in = models.DateField(verbose_name="check_in", blank=True, null=True)
    check_out = models.DateField(verbose_name="check_out", blank=True, null=True)
    special_requests = models.TextField('Special requests', max_length=10000)
    RES_STAT = (
        ('d', 'Drafted'),
        ('u', 'Unoccupied'),
        ('r', 'Reserved'),
        ('o', 'Occupied'),
    )

    status = models.CharField(
        max_length=1,
        choices=RES_STAT,
        blank=True,
        default='u',
        help_text='Reservation Status'
    )

    def __str__(self) -> str:
        return f'{self.property} {self.check_in} - {self.check_out}'

    class Meta:
        ordering = ['user', ]


class ReviewRating(models.Model):
    single_property = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='user',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
