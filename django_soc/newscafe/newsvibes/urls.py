from django.urls import path, include
from .views import SignUpView
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('search', views.search, name='search'),
     path('api-auth/', include('rest_framework.urls'))
    ]
    # path('category', views.category, name='category')