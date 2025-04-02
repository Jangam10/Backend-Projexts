from django.urls import path 
from . import views

# all urls 
urlpatterns = [
    path('', views.index,name='index')

]