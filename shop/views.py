from django.shortcuts import render, get_object_or_404
from .models import Trip, Option
import json
from django.http import HttpResponseBadRequest
from django.db.models import F


def trip_list(request):
    trips = Trip.objects.filter(max_places__gt=F('taken_places'))
    for trip in trips:
        trip.percentage = (trip.taken_places / trip.max_places) * 100

    return render(request, 'trip_list.html', {'trips': trips})

def reserve_trip(request):
    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        options_ids = request.POST.get('options')
        total_price = request.POST.get('total_price')
        
        try:
            trip = get_object_or_404(Trip, id=trip_id)
            options_ids = json.loads(options_ids)
            selected_options = Option.objects.filter(id__in=options_ids)
            print(selected_options)
            context = {
                'trip': trip,
                'selected_options': selected_options,
                'total_price': total_price
            }
            return render(request, 'reserve.html', context)
        
        except (ValueError, Trip.DoesNotExist):
            # Handle invalid JSON or non-existent trip gracefully
            return HttpResponseBadRequest("Invalid request or trip does not exist")
    
    else:
        return HttpResponseBadRequest("Invalid request method")
