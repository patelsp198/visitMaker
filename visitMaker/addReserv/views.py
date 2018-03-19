from django.shortcuts import render
from .models import Reservation
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ReservationForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReservationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/reservHome/addReserv/confirmReserv/', {'entries' : models.Reservation.objects.all()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReservationForm()

    return render(request, 'addReserv.html', {'form': form})