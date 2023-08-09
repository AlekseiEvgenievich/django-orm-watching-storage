from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
import pytz
import datetime
from datetime import timedelta

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode = passcode)
    visits = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = []
    moscow_tz = timezone.pytz.timezone('Europe/Moscow')
    
    for visit in visits:
        one_visit = {}
        one_visit['entered_at'] = visit.entered_at.astimezone(moscow_tz)
        one_visit['duration'] = visit.format_duration()
        one_visit['is_strange'] = visit.is_visit_long()
        this_passcard_visits.append(one_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
