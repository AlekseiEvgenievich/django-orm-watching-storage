from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import pytz
import datetime
from datetime import timedelta
    
def storage_information_view(request):
    # Программируем здесь
    inside_in = Visit.objects.filter(leaved_at__isnull=True)
    moscow_tz = timezone.pytz.timezone('Europe/Moscow')
    non_closed_visits = []
    for k in range(len(inside_in)):
        visit = {}
        name_person = inside_in[k].passcard.owner_name
        visit['who_entered'] = name_person
        visit_time = inside_in[k].entered_at.astimezone(moscow_tz)
        visit['entered_at'] = visit_time
        visit['duration'] = inside_in[k].format_duration()
        non_closed_visits.append(visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
