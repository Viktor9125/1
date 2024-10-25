# views.py
from django.shortcuts import render, redirect
from .forms import TeamEventForm, EventForm
from .models import Team, Event
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date


def home(request):
    return render(request, 'event_list.html')


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        date = parse_date(form['date'])
        query_date = request.GET.get(date=date)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def assign_team_event(request):
    if request.method == 'POST':
        form = TeamEventForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            event = form.cleaned_data['event']
            team.event = event  # Привязка мероприятия к команде
            team.save()  # Сохранение изменений в базе данных
            return redirect('home')  # Замените 'success' на вашу целевую страницу
    else:
        form = TeamEventForm()
    return render(request, 'assign_team_event.html', {'form': form})
