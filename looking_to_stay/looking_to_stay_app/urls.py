from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>', views.HotelDetailView.as_view(), name='hotel'),
    path('about_us/', views.about_us, name='about_us'),
    path('reservation/', views.UserReservationCreateView.as_view(), name='reservation'),
    path('myreservations/', views.UserHotelListView.as_view(), name='user_reservations')
]