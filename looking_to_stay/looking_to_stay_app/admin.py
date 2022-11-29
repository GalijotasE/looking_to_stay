from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    readonly_fields = ('id',)
    #list_editable = ('category_name',)
    search_fields = ('id', 'category_name')

admin.site.register(models.Category, CategoryAdmin)