from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path('register/', views.register_request),
    path('login/', views.login_request),
    path('logout/', views.logout),
]

