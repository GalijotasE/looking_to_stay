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


# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'company_name')
#     readonly_fields = ('id', )
#     search_fields = ('company_name', )
#     fieldsets = (
#         ('General', {'fields':('id', 'company_name')}),
#         ('Contact Info', {'fields':('email', 'phone_number', 'postal_code', 'address')})
#     )


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'city', 'category')
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
    list_display = ('id', 'price', 'people')
    readonly_fields = ('id',)
    list_display_links = ('price',)


class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'amenity')
    readonly_fields = ('id', )
    list_display = ('amenity',)
    search_fields = ('amenity',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_name', 'room_type_id' )
    readonly_fields = ('id',)
    list_display = ('room_name',)
    search_fields = ('room_name', 'room_type_id')


admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.City, CityAdmin)
# admin.site.register(models.Company)
admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.RoomType, RoomTypeAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Amenities, AmenitiesAdmin)