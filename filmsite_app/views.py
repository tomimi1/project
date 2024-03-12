from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Film
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def home_page(request):
    return render(request, './films/index.html')

def all_films_page(request):
    films = Film.objects.all()[:10]
    genres = Genre.objects.all()
    context = {
        'genres': genres,
        'films': films
    }
    return render(request, './films/all_films.html', context)

def top_films_page(request):
    films = Film.objects.all()
    genres = Genre.objects.all()
    context = {
        'genres': genres,
        'films': films
        }
    return render(request, './films/top_films.html', context)

def films_by_category_page(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    genres = Genre.objects.all()
    films = Film.objects.filter(genre=genre)
    context = {
        'genres': genres, 
        'genre': genre,
        'films': films
        }
    return render(request, './films/films_by_category.html', context)

def films_by_search_page(request):
    query = request.GET.get("query")
    genres = Genre.objects.all()
    films = Film.objects.filter(name__icontains=query) | Film.objects.filter(description__icontains=query)
    context = {
        'genres': genres, 
        "query": query,
        "films": films
    }
    return render(request, './films/films_by_search.html', context)

def film_detail_page(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {
        'film': film
        }
    return render(request, './films/film_detail.html', context)

def add_film_page(request):
    return render(request, './admin/add_film.html')

def add_genre_page(request):
    return render(request, './admin/add_genre.html')


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login_page")
    else:
        form = NewUserForm()
    return render(request, './user/sign-up.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("top_films_page")
    else:
        form = AuthenticationForm()
    return render(request, './user/login.html', {'form': form})

def logout_action(request):
    logout(request)
    return redirect("home_page")