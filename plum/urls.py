from django.conf.urls import url
from plum import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^logowania$', views.logowaniaApi),
    url(r'^pracownicy$', views.pracownicyApi),
    
] 