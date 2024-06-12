from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html') 

def floor(request):
    return render(request, 'core/floor.html')

def services(request):
    return render(request, 'core/services.html')

def shower(request):
    return render(request, 'core/shower.html')

def move(request):
    return render (request, 'core/move.html')

def surface(request):
    return render (request, 'core/surface.html')

def window(request):
    return render (request, 'core/window.html')

def carpet(request):
    return render (request, 'core/carpet.html')

def login(request):
    return render (request, 'core/login.html')

def eventsclean(request):
    return render (request, 'core/eventsclean.html')

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        day = request.POST.get('day')
        time = request.POST.get('time')
        service = request.POST.get('service')

        
        send_mail(
            'New Service Enquiry',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {day}\nService: {service}\nTime: {time}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

    return render (request, 'core/book.html')

def enquire(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        day = request.POST.get('day')
        time = request.POST.get('time')
        service = request.POST.get('service')

        
        send_mail(
            'New Service Enquiry',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {day}\nService: {service}\nTime: {time}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

    return render (request, 'core/enquire.html')
