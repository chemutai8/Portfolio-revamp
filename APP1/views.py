from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def expertise(request):
        return render(request,'expertise.html')


def experience(request):
        return render(request,'experience.html')


def contact(request):
        return render(request,'contact.html')


