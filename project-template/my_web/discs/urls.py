from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.DiscCreateView.as_view(), name='add_disc'),
    path('list/', views.DiscListView.as_view(), name='disc_list'),
    path('<int:pk>/', views.DiscDetailView.as_view(), name='disc_detail'),
    #path('search/', views.search_book, name='search_book'),
]