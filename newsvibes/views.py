from turtle import title
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from django.shortcuts import HttpResponse
from .models import NEWS, Person
from rest_framework import viewsets
from .serializers import Newsserializer, Personserializer, Userserializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
import random


api_key='cd8b0420d24541a69eff42513ab87798'

# Create your views here.


class NewsView(viewsets.ModelViewSet):
    serializer_class = Newsserializer
    queryset = NEWS.objects.all()
    #permission_classes = (IsAuthenticated,)

class PersonView(viewsets.ModelViewSet):
    serializer_class = Personserializer
    queryset = Person.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()

# class NewsDetails(viewsets.ModelViewSet):
#     def put(self, request, id):
#         print(request)
#         print(request.data)
#         data = NEWS.objects.get(id = id)
#         serializer = Newsserializer(data, data=request.data)
#         serializer.save()

def put(request, id):
    print(Newsserializer(request.data))
    data = NEWS.objects.get(id = id)
    print(data)

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

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

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user_id = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        user_id.save()
        verification_code = random.randint(100000, 999999)
        print(verification_code)
        new_person = Person(
            user = user_id,
            username = username,
            password = password,
            token = verification_code
        )
        new_person.save()
        subject = "verification for newscafe app"
        message = f"your verification code is {verification_code}"
        mail_from = settings.EMAIL_HOST_USER
        mail_to = [email]
        send_mail(subject, message, mail_from, mail_to)
        return redirect('../checkmail')

    return render(request, 'registration/signup.html')

def verify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        verification_code = request.POST.get('verification_code')
        print(verification_code)
        print(username)
        person = Person.objects.filter(username = username, password = password).first()
        print(person.username)
        print(person.password)
        print(person.token)
        if person.token == str(verification_code):
            print(person.is_verified)
            person.is_verified = True
            print(person.is_verified)
            print('true')
        else:
            print('false')
        person.save()
        return redirect('http://localhost:3000/')

    return render(request, 'registration/checkmail.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_id = User.objects.filter(username = username, password= password).first()
        if user_id is None:
            messages.success(request, 'user not found')
            return redirect('http://localhost:3000/login/')

        person = Person.objects.filter(user = user_id).first()
            
        if person.is_verified == False:
            messages.success(request, 'you are not verified. check mail')
            return redirect('/')
        else:
            user = authenticate(username = username, password = password)
            print(user)
            login(request, user)
            return redirect('../../')
        
        user = authenticate(username = username)
        '''print(user)
        if user is None:
            messages.success(request, 'wrong password')
            return redirect('/')'''

        login(request, user)
        return redirect('../../')

    return render(request, 'registration/login.html')