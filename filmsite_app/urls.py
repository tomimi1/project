from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('films/all/', views.all_films_page, name='all_films_page'),
    path('films/top/', views.top_films_page, name='top_films_page'),
    path('films/category/<slug:slug>/', views.films_by_category_page, name='films_by_category_page'),
    path('films/search/', views.films_by_search_page, name='films_by_search_page'),
    path('films/detail/<int:pk>/', views.film_detail_page, name='film_detail_page'),

    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]