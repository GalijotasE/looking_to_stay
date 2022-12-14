from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Hotel, Country, Category, Reservation, ReviewRating
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import ReservationForm, ReviewForm


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


class SearchResultsView(ListView):
    model = Hotel
    template_name = 'lookingtostay/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        property_list = Hotel.objects.filter(
            Q(city__city_name__icontains=query) | Q(hotel_name__icontains=query) | Q(address__icontains=query)
        )
        return property_list


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'lookingtostay/hotel_detail.html'

    def hotel(request, hotel_id):
        single_hotel = get_object_or_404(Hotel, pk=hotel_id)
        review = ReviewRating.objects.filter(single_property = single_hotel)

        return render(request, 'lookingtostay/hotel_detail.html', {'hotel': single_hotel, 'review': review})


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

    def hotel(request, hotel_id):
        single_hotel = get_object_or_404(Hotel, pk=hotel_id)
        review = ReviewRating.objects.filter(single_property = single_hotel)

        return render(request, 'lookingtostay/hotes.html', {'review': review})


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


class UserReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'lookingtostay/reservation.html'
    success_url = reverse_lazy('user_reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'r'
        return super().form_valid(form)

    def test_func(self):
        reservation = self.get_object()
        return self.request.user == reservation.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation'] = self.get_object()
        if context['reservation'].status == 'r':
            context['action'] = 'Edit Reservation'
        return context


class UserReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    template_name = 'lookingtostay/reservation_delete.html'
    success_url = reverse_lazy('user_reservations')

    def test_func(self):
        reservation = self.get_object()
        return self.request.user == reservation.user

    def form_valid(self, form):
        reservation = self.get_object()
        if reservation.status == 'r':
            pass
        return super().form_valid(form)

def submit_review(request, property_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, single_property__id=property_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            # messages.success(request, 'Thank you! Your review has been updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.single_property_id = property_id
                data.user_id = request.user.id
                data.save()
                # messages.success(request, 'Thank you! Your review has been submitted')
                return redirect(url)
    context = {
        ''
    }