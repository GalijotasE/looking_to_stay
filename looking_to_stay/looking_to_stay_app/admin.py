from django.contrib import admin
from . import models

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
    readonly_fields = ('id',)
    search_fields = ('country_name',)
    list_display_links = ('country_name', )


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'country_id')
    readonly_fields = ('id',)
    search_fields = ('city_name',)
    list_display_links = ('city_name',)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'city', 'category',)
    readonly_fields = ('id', )
    search_fields = ('hotel_name', 'city')
    list_display_links = ('hotel_name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    readonly_fields = ('id',)
    search_fields = ('category_name',)
    list_display_links = ('category_name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency')
    readonly_fields = ('id', )
    list_display_links = ('currency',)


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price','currency_type', 'people')
    readonly_fields = ('id',)
    list_display_links = ('name',)


class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'amenity')
    readonly_fields = ('id', )
    search_fields = ('amenity',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'roomtype')
    list_display_links = ('user', 'property')
    search_fields = ('user', 'property')

admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.RoomType, RoomTypeAdmin)
admin.site.register(models.Amenities, AmenitiesAdmin)
admin.site.register(models.HotelImage)
admin.site.register(models.Reservation, ReservationAdmin)