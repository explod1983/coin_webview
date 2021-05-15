from django.shortcuts import render
from .models import Coin
import json

with open('my_cryptocoins.json') as json_file:
    db = json.loads(json_file.read())
# print(db)


def home(request):
    context = {
        'coins': Coin.objects.all()
    }
    return render(request, 'morda/home.html', context)
