from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, carpet, services, floor, shower, surface, window, move, login, book, eventsclean, enquire, thank_you


urlpatterns = [
    path('', index, name='index'),
    path('carpet-cleaning/', carpet, name='carpet'),
    path('services/', services, name='services'),
    path('floor-cleaning/', floor, name='floor'),
    path('shower-cleaning/', shower, name='shower'),
    path('surface-cleaning/', surface, name='surface'),
    path('window-cleaning/', window, name='window'),
    path('move-cleaning/', move, name='move'),
    path('sustainability/', login, name='login'),
    path('book/', book, name='book'),
    path('eventsclean/', eventsclean, name='eventsclean'),
    path('enquire/', enquire, name='enquire'),
    path('thank-you/', thank_you, name='thank_you'),
    path('', include('newsletter.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
