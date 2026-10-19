from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base , name="base"),
    path('login/', views.login , name="login"),
    path('register/', views.register , name="register"),
    path('dashboard/', views.dashboard , name="dashboard"),
]
