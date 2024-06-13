from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber
from django.conf import settings

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email_address')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)

                # Send notification to admin
                send_mail(
                    'New Newsletter Subscription',
                    f'New subscription from: {email}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )

                
                send_mail(
                    'Subscription Confirmed',
                    'Thank you for subscribing to our newsletter!',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Subscription successful!')
            else:
                messages.info(request, 'Email is already subscribed!')
        else:
            messages.error(request, 'Please enter a valid email address.')
    
    return redirect('index')  

