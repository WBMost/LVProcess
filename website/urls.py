from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('index.html', views.index, name = "index"),
    path('contact.html',views.contact, name = "contact"),
    path('404.html', views.error404, name = "404"),
]
