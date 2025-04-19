from django.urls import path
from . import views
app_name = 'deen_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
   
]
