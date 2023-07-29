
from django.contrib import admin
from django.urls import path
from news.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home_url"),
    path('news/',news, name="news_url"),
    path('detail/<str:title>/',news_detail, name="detail_url"),
    
]
