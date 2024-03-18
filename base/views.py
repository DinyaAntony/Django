from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Age 15-19'},
#     {'id':2, 'name': 'Age 20-24'},
#     {'id':3, 'name': 'Age 25-29'},
#     {'id':4, 'name': 'Age 30-39'},
#     {'id':5, 'name': 'Age 40-49'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)