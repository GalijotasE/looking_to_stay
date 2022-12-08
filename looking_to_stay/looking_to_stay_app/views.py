from django.shortcuts import render
from .models import Hotel, Country, Category, Amenities
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse


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


# def hotels(request):
#     paginator = Paginator(Hotel.objects.all(), 10)
#     page_number = request.GET.get('page')
#     paged_hotels = paginator.get_page(page_number)
#     return render(request, 'lookingtostay/hotels.html', {'hotels': paged_hotels})


def locations(request):
    return render(request, 'lookingtostay/locations.html', )

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'lookingtostay/hotel_detail.html'

    def hotel(request, hotel_id):
        single_hotel = get_object_or_404(Hotel, pk=hotel_id)
        return render(request, 'lookingtostay/hotel_detail.html', {'hotel': single_hotel})

    # def all_amenities(request):
    #     single_amenity = Hotel.amenities.all()
    #     return render(request, 'lookingtostay/hotel_detail.html', {'single_amenity': single_amenity})


    # def get_success_url(self):
    #     return reverse('hotel', kwargs={'pk': self.get_object().id})


class HotelListView(ListView):
    model = Hotel
    paginate_by = 10
    template_name = 'lookingtostay/hotels.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset.filter(Q(hotel_name__icontains=search) | Q(description__icontains=search))
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels_count'] = self.get_queryset().count()
        category_id = self.request.GET.get('category_id')
        context['categories'] = Category.objects.all()
        if category_id:
            context['category'] = get_object_or_404(Category, id=category_id)
        return context

def makereservation(request):
    return render(request, 'lookingtostay/reservation.html')
