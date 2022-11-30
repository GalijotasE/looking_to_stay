from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel, Country, Category

def index(request):
    num_hotels = Hotel.objects.all().count()
    num_countries = Country.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_hotels': num_hotels,
        'num_countries': num_countries,
        'num_categories': num_categories,
    }

    return render(request, 'lookingtostay/index.html', context=context)

def hotels(request):
    return render(request, 'lookingtostay/hotels.html',)

def locations(request):
    return render(request, 'lookingtostay/locations.html',)