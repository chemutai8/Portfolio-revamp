from django.urls import path

from . import views

urlpatterns=[
path('',views.index,name='index'),
path('/expertise',views.index,name='expertise'),
path('/experience',views.experience,name='experience'),
path('/contact',views.contact,name='contact'),

]