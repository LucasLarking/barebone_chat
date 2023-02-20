from django.shortcuts import render, redirect
from .models import Room
from .forms import Create_room_form, Create_message_form, search_room_form



def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'search_room_form': search_room_form
    }

    if request.method == 'POST':
        form = search_room_form(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('name')
            print(form.cleaned_data)
            print(search_term)
            rooms = Room.objects.filter(name__icontains=search_term)
            context = {
                'rooms': rooms,
                'search_room_form': search_room_form
            }
            return render(request, 'base/home.html', context)
    return render(request, 'base/home.html', context)


def create_room(request):
    form = Create_room_form()

    if request.method == 'POST':  # Validera datan när ett formulär skickats in
        form = Create_room_form(request.POST)
        if form.is_valid():
            form.save()
            # skicka til lbaka användaren till startsidan
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'base/create_room.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)  # Get corresponding room
    # få alla meddelanden tillhörande tråden
    room_messages = room.message_set.all()
    form = Create_message_form()

    if request.method == 'POST':
        form = Create_message_form(request.POST)
        if form.is_valid():

            message = form.save(commit=False)
            message.room = room
            message.save()
            return redirect('room', pk=room.id)

    context = {
        'room': room,
        'room_messages': room_messages,
        'form': form
    }
    return render(request, 'base/room.html', context)
