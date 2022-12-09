from django.contrib.auth import get_user_model
from django import forms
from . models import Reservation, ReviewRating
from django.utils.timezone import datetime, timedelta


class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('user', 'first_name', 'last_name', 'country', 'city',
        'post_code', 'address', 'property', 'roomtype',
        'check_in', 'check_out', 'special_requests',
        )
        widgets = {
            'user': forms.HiddenInput(),
            'check_in': DateInput(),
            'check_out': DateInput(),
            }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ('subject', 'review', 'rating')