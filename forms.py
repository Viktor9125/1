from django import forms
from .models import Event, Team


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'guests', 'budget', 'description', 'date']

class TeamEventForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Выберите команду")
    events = forms.ModelChoiceField(queryset=Event.objects.all(), label="Выберите мероприятие")


