from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('this is the dynamo app')

def cars(request):
    mycars = [
        {'make':'Ferrari', 'model': 'Portofino M', 'type': 'Supercar', 'price': '250000', 'site': 'https://www.ferrari.com/en-EN/auto/ferrari-portofino-m', 'image': 'ferrari.jpg'},
        {'make':'Jeep', 'model': 'Wrangler Rubicon 4xe', 'type': 'Off-road SUV', 'price': '50000', 'site': 'https://www.jeep.com/wrangler-4xe.html', 'image': 'jeep.jpeg'},
        {'make':'Chevrollet', 'model': 'Camaro 69 Z28', 'type': 'Muscle car', 'price': '20000-25000', 'site': 'https://heacockclassic.com/articles/1969-chevrolet-camaro-z28-the-other-pony-car/', 'image': 'camaro.jpeg'}
    ]
    
    return render(
        request, 
        'dynamo/cars.html',
        {
            'cars': mycars,
            'condition': True
        }
    )
