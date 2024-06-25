from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import requests
from django.db.models import Avg
from django.views.generic import DetailView

from .models import Brewery, Review, BrewPub


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def search_view(request):
    query = request.GET.get('query', '')
    search_by = request.GET.get('search_by', 'by_city')
    if search_by == 'by_city':
        url = f'https://api.openbrewerydb.org/breweries?by_city={query}'
    elif search_by == 'by_name':
        url = f'https://api.openbrewerydb.org/breweries?by_name={query}'
    elif search_by == 'by_type':
        url = f'https://api.openbrewerydb.org/breweries?by_type={query}'
    response = requests.get(url)
    breweries = response.json()
    return render(request, 'search.html', {'breweries': breweries})


def brewery_detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, id=brewery_id)
    reviews = Review.objects.filter(brewery=brewery)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        description = request.POST.get('description')
        review = Review(user=request.user, brewery=brewery, rating=rating, description=description)
        review.save()
        # Update brewery rating
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        brewery.rating = average_rating
        brewery.save()
    return render(request, 'brewery_detail.html', {'brewery': brewery, 'reviews': reviews})

# def brewery_detail(request, brewery_id):
#     try:
#         brewery = get_object_or_404(BrewPub, id=brewery_id)
#         reviews = Review.objects.filter(brewery=brewery)
#
#         # Handle POST request for adding reviews
#         if request.method == 'POST':
#             rating = request.POST.get('rating')
#             description = request.POST.get('description')
#             review = Review(user=request.user, brewery=brewery, rating=rating, description=description)
#             review.save()
#
#             # Update brewery rating if needed
#             average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
#             brewery.rating = average_rating
#             brewery.save()
#
#         return render(request, 'brewery_detail.html', {'brewery': brewery, 'reviews': reviews})
#
#     except BrewPub.DoesNotExist:
#         # Handle case where BrewPub with given UUID does not exist
#         return HttpResponse("BrewPub not found. Please check the UUID or go back to search.")

