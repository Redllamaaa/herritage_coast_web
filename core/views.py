from django.shortcuts import render
from dashboard.models import Staff

def home(request):
    featured_staff = Staff.objects.filter(show_on_homepage=True)
    return render(request, "home.html", {"featured_staff": featured_staff})

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    return render(request, 'reviews.html')

def contact(request):
    return render(request, 'contact.html')
