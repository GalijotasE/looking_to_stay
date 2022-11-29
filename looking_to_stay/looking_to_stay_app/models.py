from django.db import models


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
        ordering = ['city_name', 'country_id']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Company(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    company_name = models.CharField('Company Name', max_length=128, help_text='Please type a name of the company')
    email = models.CharField('Email', max_length=128)
    postal_code = models.CharField('Postal Code', max_length=10)
    address = models.CharField('Address', max_length=255)

    def __str__(self) -> str:
        return {self.company_name}

    class Meta():
        ordering = ['company_name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Category(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    category_name = models.CharField('Category', max_length=128, help_text='Please type a name of the category')

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Hotel(models.Model):
    id = models.AutoField('Unique ID', primary_key=True)
    hotel_name = models.CharField('Hotel Name', max_length=100, help_text="Please enter a name of the Hotel")
    description = models.TextField('Description', max_length=10000,
        help_text='Please enter a description of the hotel, consisting up to 10000 words.')
    company_id = models.ForeignKey(
        Company, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    city_id = models.ForeignKey(
        City, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    cover_photo = models.ImageField('Cover Photo', upload_to='covers', blank=True, null=True)

    def __str__(self) -> str:
        return self.hotel_name

    class Meta:
        ordering = ['hotel_name', 'company_id']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


# class Room(models.Model):
#     pass


# class RoomType(models.Model):
#     pass


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