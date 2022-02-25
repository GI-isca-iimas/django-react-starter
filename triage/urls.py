from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('diego', views.index_diego)
]
