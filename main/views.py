from django.shortcuts import render, redirect
from shop.models import Trip
from django.db.models import F
from .models import Division
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def index(request):
    """
    Display the index page.

    **Template**

    :template:`index.html`

    """
    return render(request, "index.html")

def underconstruction(request):
    return render(request, 'underconstruction.html')

def about(request):
    return render(request, 'about.html')

def termsconditions(request):
    return render(request, 'terms-conditions.html')

def privacypolicy(request):
    return render(request, 'privacy-policy.html')

@xframe_options_exempt
def contact(request):
    return render(request, 'contact.html')

def trips_view(request):
    trips = Trip.objects.filter(max_places__gt=F('taken_places')).order_by('-start_date')[:3]
    
    for trip in trips:
        trip.percentage = (trip.taken_places / trip.max_places) * 100

    return render(request, 'trips.html', {'trips': trips})

@xframe_options_exempt
def divisions(request):
    divisions = Division.objects.all()
    for division in divisions:
        division.percentage = division.percentage()
        division.status = "Full" if division.percentage >= 100 else "Looking"
    
    return render(request, 'divisions.html', {'divisions': divisions})