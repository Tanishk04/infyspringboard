
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
    path('feedback/', views.feedback, name='feedback'),
    path('events.html', views.events, name='events'),
    path('booking.html', views.booking, name='booking'),
    path('success.html', views.success, name='success'),
    path('gallery.html', views.gallery, name='gallery'),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.index, name='index'),  # Add this line

]
