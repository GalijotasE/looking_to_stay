from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>', views.HotelDetailView.as_view(), name='hotel'),
    path('locations/', views.locations, name='locations'),
]