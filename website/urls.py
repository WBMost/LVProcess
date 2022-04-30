from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('contact.html',views.contact, name = "contact"),
    path('404.html', views.error404, name = "404"),
    path('testimonials.html', views.testimonials, name = "testimonials"),
    path('order.html', views.order, name = "order"),
]
