from turtle import title
from urllib import response
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from django.shortcuts import HttpResponse
from .models import NEWS
from rest_framework import viewsets
from .serializers import Newsserializer


api_key='cd8b0420d24541a69eff42513ab87798'

# Create your views here.


class NewsView(viewsets.ModelViewSet):
    serializer_class = Newsserializer
    queryset = NEWS.objects.all()

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')
    if country and category:
        api_url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
        response=requests.get(api_url)
        data_as_json=response.json() 
        data_articles=data_as_json['articles']
        
    else:
        api_url = f'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={api_key}'
        response=requests.get(api_url)
        data_as_json=response.json()  
        data_articles=data_as_json['articles']
    

    for article in data_articles:
        p = NEWS(
            title = article['title'],
            description = article['description'],
            Newsurl = article['url'],
            Imageurl = article['urlToImage'],
            publishedAt = article['publishedAt']
        )
        p.save()

    dict1={'data_articles': data_articles}
    return render(request, 'home.html', dict1)


def search(request):
    searched_news=request.GET.get('search')
    api_url = f'https://newsapi.org/v2/everything?q={searched_news}&from=2022-05-07&sortBy=publishedAt&apiKey={api_key}'
    response=requests.get(api_url)
    data_as_json=response.json()  
    data_articles=data_as_json['articles']
    dict1={'data_articles':data_articles} 
    return render(request, 'search.html', dict1)


# def category(request):
#     category=request.GET.get('category')
#     if category:
#         api_url = f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}'
#         response=requests.get(api_url)
#         data_as_json=response.json()  
#         data_articles=data_as_json['articles']
        
#     else:
#         api_url = f'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={api_key}'
#         response=requests.get(api_url)
#         data_as_json=response.json()  
#         data_articles=data_as_json['articles']
    
#     dict1={'data_articles':data_articles}
#     return render(request, 'category.html', dict1)
        
    

    
# countries={"ae": "United Arab Emirates", "ar": "Argentina", "at":"Austria", "au":"Australia",
    # "be":"Belgium","bg":"Bulgaria","br":"Brazil","ca":"Canada","ch":"Switzerland","cn":"China",
    # "co":"Colombia","cu":"Cuba","cz":"Czech Republic", "de":"Germany","eg":"Egypt","fr":"France",
    # "gb":"United Kingdom", "gr":"Greece","hk":"HongKong", "hu":"Hungary","id":"Indonesia","ie":"Ireland",
    # "il":"Israel","in": "India","it":"Italy", "jp":"Japan","kr":"South Korea","lt":"Lithuania","lv":"Latvia",
    # "ma":"Morocco","mx":"Mexico","my":"Malaysia","ng":"Nigeria","nl":"Netherlands","no":"Norway","nz":"New Zealand",
    # "ph":"Philippines","pl":"Poland","pt":"Portugal","ro":"Romania","rs":"Serbia","ru":"Russia","sa":"Saudi Arabia",
    # "se":"Sweden","sg":"Singapore","si":"Slovenia","sk":"Slovakia","th":"Thailand","tr":"Turkey","tw":"Taiwan",
    # "ua":"Ukraine","us":"United States","ve":"Venezuela","za":"South Africa"}
