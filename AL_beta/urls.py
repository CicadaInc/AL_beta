from django.contrib import admin
from django.urls import path
from search import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search),
    path('admin/', admin.site.urls),
]
