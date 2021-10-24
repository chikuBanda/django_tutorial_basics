from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location': 'Paris',
            'slug': 'a-second-meetup'
        }
    ]

    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetups_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First meetup',
        'description': 'this is a first meetups'
    }

    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })


def myview(request):
    # return HttpResponse('THIS IS MY VIEW')
    return render(request, 'meetups/index.html')
