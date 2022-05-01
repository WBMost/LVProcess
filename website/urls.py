from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('contact.html',views.contact, name = "contact"),
    path('404.html', views.error404, name = "404"),
    path('testimonials.html', views.testimonials, name = "testimonials"),
    path('order.html', views.order, name = "order"),
    path('pricing.html', views.pricing, name = "pricing"),
    path('services.html', views.services, name = "services"),
    path('thanks.html', views.thanks, name = "thanks"),
    path('/#about', views.about, name = "about"),
    path('payment.html', views.payment, name = "payment"),
]
