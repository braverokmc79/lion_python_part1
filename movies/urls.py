from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    
    path('movies/', views.movie_list, name='movies'),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    
    path('page/<str:id>/', views.str_page, name='str_page'),
]

