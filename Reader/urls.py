from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.redirect, name="form"),
    path('book/', include('Book.urls'))
]