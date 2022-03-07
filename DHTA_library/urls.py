"""DHTA_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from welcome import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('catalog/', views.catalog, name= 'catalog'),
    path('book_detail/<int:id>', views.book_detail, name = 'book_detail'),
    path('register/', views.registration, name = 'registration'),
    path('api/',views.api_book_list),
    path('api/<int:pk>/', views.api_book_detail),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
