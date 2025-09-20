from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    return render(request, 'reviews.html')

def contact(request):
    return render(request, 'contact.html')
