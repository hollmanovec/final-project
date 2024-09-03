from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.discs, name='discs'),
    path('add/', views.DiscCreateView.as_view(), name='add_disc'),
    path('list/', views.DiscListView.as_view(), name='disc_list'),
    path('<int:pk>/', views.DiscDetailView.as_view(), name='disc_detail'),
    path('<int:pk>/delete/', views.DiscDeleteView.as_view(), name='disc_delete'),
    path('<int:pk>/update/', views.DiscUpdateView.as_view(), name='disc_update'),
    path('search/', views.search_disc, name='search_disc'),
]
