from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import pytz
import datetime
from datetime import timedelta
    
def storage_information_view(request):
    inside_in = Visit.objects.filter(leaved_at__isnull=True)
    moscow_tz = timezone.pytz.timezone('Europe/Moscow')
    non_closed_visits = []
    for user in inside_in:
        visits = {'who_entered': user.passcard.owner_name ,
                'entered_at': user.entered_at.astimezone(moscow_tz),
                'duration': user.format_duration(),
                }
        non_closed_visits.append(visits)
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
