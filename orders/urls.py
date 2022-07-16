from django.urls import path
from . import views


urlpatterns = [
    path("main", views.home, name= 'home'),
    path("yetkili/<int:id>", views.authorizedUser, name= 'yetkili'),
    path("searchdate", views.searchdate, name= 'searchdate'),
    path("search", views.search, name= 'search'),
    path("teslim/<int:id>", views.teslim, name= 'teslim'),
    path("main/<int:id>", views.addAppointment, name= 'randevuekle'),
    path("<int:id>/main", views.deleteAppointment, name= 'randevusil'),
]