from django.shortcuts import render
import json

with open('my_cryptocoins.json') as json_file:
    db = json.loads(json_file.read())
# print(db)


def home(request):
    context = {
        'coins': db['coins']
    }
    return render(request, 'morda/home.html', context)
