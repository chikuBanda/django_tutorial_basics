from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # ourdomain.com/meetups
    path('myview/', views.myview),
    # our-domain.com/meetups/<dynamic-path-segment>
    path('meetup/<slug:meetup_slug>', views.meetups_details)
]
