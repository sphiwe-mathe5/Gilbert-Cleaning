from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, carpet, services, floor, shower, surface, window, move, login, book, eventsclean, enquire


urlpatterns = [
    path('', index, name='index'),
    path('carpet/', carpet, name='carpet'),
    path('services/', services, name='services'),
    path('floor/', floor, name='floor'),
    path('shower/', shower, name='shower'),
    path('surface/', surface, name='surface'),
    path('window/', window, name='window'),
    path(' move/', move, name='move'),
    path('login/', login, name='login'),
    path('book/', book, name='book'),
    path('eventsclean/', eventsclean, name='eventsclean'),
    path('enquire/', enquire, name='enquire'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
