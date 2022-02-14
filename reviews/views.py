from django.shortcuts import render
from .models import Article


def home(request):
    article = Article.objects.all()
    return render(request, 'reviews/home.html', {"title": "Главная страница", 'article': article})


def about(request):
    return render(request, 'reviews/about.html', {"title": "Про нас"})


def register(request):
    return render(request, 'reviews/register.html', {"title": "Регистрация"})



