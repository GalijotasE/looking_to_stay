from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Hotel, Country, Category, Reservation
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import ReservationForm


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


def about_us(request):
    return render(request, 'lookingtostay/about_us.html', )


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'lookingtostay/hotel_detail.html'

    def hotel(request, hotel_id):
        single_hotel = get_object_or_404(Hotel, pk=hotel_id)
        return render(request, 'lookingtostay/hotel_detail.html', {'hotel': single_hotel})


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


class UserHotelListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'lookingtostay/user_reservation_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user).order_by('property')
        return queryset
        
class UserReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'lookingtostay/reservation.html'
    success_url = reverse_lazy('user_reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'r'
        return super().form_valid(form)
    
class UserReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'lookingtostay/reservation_detail.html'

    def reservation(request, reservation_id):
        single_reservation = get_object_or_404(Reservation, pk=reservation_id)
        return render(request, 'lookingtostay/reservation_detail.html', {'reservation': single_reservation})