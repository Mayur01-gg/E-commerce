from django.urls import path
from grocery import views

urlpatterns = [
    path('grocery/', views.grocery, name="grocery")
]