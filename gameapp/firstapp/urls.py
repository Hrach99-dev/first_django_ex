from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('runner', views.runner, name='runner'),
    path('game', views.game, name='game'),
    path('addquest', views.addquest, name='addquest'),
    
]