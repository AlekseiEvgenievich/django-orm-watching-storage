from django.db import models
from django.utils import timezone
import pytz
import datetime
from datetime import timedelta

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )/Users/aleksejsmirnov/projectpython/django-orm-watching-storage/datacenter/models.py
    
    def get_duration(self):
        moscow_tz = timezone.pytz.timezone('Europe/Moscow')
        if self.leaved_at is None:
            differ = (timezone.localtime().astimezone(moscow_tz) - self.entered_at.astimezone(moscow_tz))
        else:
            differ = (self.leaved_at.astimezone(moscow_tz)- self.entered_at.astimezone(moscow_tz))
        return differ
    
    def is_visit_long(self, minutes=60):
        duration = self.get_duration()
        return duration > timedelta(minutes=minutes)
    
    def format_duration(self):
        duration = self.get_duration()
        return str(duration).split(".")[0]
