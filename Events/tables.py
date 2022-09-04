import django_tables2 as tables
from Models.models import Events


class EventsTable(tables.Table):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date']