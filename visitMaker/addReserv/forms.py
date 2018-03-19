from django import forms
from django.forms import ModelForm, Textarea
from .models import Reservation

# form completely dependent on base model
class ReservationForm(ModelForm):
	class Meta:
		model = Reservation
		fields = '__all__'
		widgets = {
			'Special_Accomidations': Textarea(),
		}