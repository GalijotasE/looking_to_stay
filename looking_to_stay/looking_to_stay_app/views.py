from django.shortcuts import render
from .models import Hotel, Country, Category
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


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
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'lookingtostay/hotels.html', context=context)


def locations(request):
    return render(request, 'lookingtostay/locations.html', )

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'