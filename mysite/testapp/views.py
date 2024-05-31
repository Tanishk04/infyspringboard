from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserInfoForm1, BookingForm
from .models import UserInfo1, Event
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User
def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form = UserInfoForm1(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            address = form.cleaned_data['address']
            phoneno = form.cleaned_data['phoneno']
            password = form.cleaned_data['password']

            # Hash the password
            hashed_password = make_password(password)

            # Create and save the user
            new_user = UserInfo1(name=name, mail=mail, address=address, phoneno=phoneno, password=hashed_password)
            new_user.save()

            return redirect('success')
    else:
        form = UserInfoForm1()
    return render(request, 'register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserInfo1.objects.get(mail=email)
        except UserInfo1.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')
        if check_password(password, user.password):
            # Log the user in by setting session variables or similar
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            messages.success(request, f'Login successful! Welcome, {user.name}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')
def index(request):
    return render(request, 'main.html')

def feedback(request):
    return render(request, 'feedback.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    events_list = Event.objects.all()
    return render(request, 'events.html', {'events': events_list})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
