from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
   return render(request, "home.html")


def news(request):
   news  = Blog.objects.all()

   return render(request, "news.html",{'news':news})

   
def news_detail(request, title):
   single_news = Blog.objects.filter(title = title).first()
   print(single_news)
   return render(request, "news-detail.html", {'title':single_news})