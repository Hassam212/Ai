from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_item, name='add'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('search/', views.search_venues, name='search-venues'),
    path('card/', views.card, name='card')

]
