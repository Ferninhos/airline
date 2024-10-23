from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/flights.html', {
        'flight': flight,
        'passangers': flight.passanger.all()
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        request.POST['passanger']