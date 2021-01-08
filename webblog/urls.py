from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',include('blog.urls')),
    path('reviews/',include('reviews.urls')),
    path('technology/',include('technology.urls')),
    path('festival/',include('festival.urls')),
    path('sports/',include('sports.urls')),
    path('news/',include('news.urls')),
    path('places/',include('places.urls')),
]
