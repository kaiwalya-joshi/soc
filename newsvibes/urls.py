from django.urls import path, include
# from .views import SignUpView
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login1),
    path('checkmail', views.verify),
    path('search', views.search, name='search'),
     path('api-auth/', include('rest_framework.urls')),
    path('api/articles/<id>', views.put)
    ]
    # path('category', views.category, name='category')