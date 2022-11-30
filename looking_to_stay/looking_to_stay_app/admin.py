from django.contrib import admin
from . import models

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
    readonly_fields = ('id',)
    search_fields = ('country_name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'country_id')
    readonly_fields = ('id',)
    search_fields = ('city_name',)


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





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    readonly_fields = ('id',)
    search_fields = ('category_name',)



admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.City)
# admin.site.register(models.Company)
admin.site.register(models.Hotel)
admin.site.register(models.Category, CategoryAdmin)