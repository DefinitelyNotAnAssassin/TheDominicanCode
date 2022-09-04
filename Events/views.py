from django.shortcuts import render
from Models.models import Events
from .tables import EventsTable
from calendar import HTMLCalendar
# Create your views here.


def event_page(request):
    events_ = Events.objects.all().order_by('event_date')
    items = {
        'table': EventsTable(events_)
    }
    return render(request, 'Events/events.html', context=items)
