"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('Company',views.CompanyViewset,basename='Company')


from . import views
from . import views1
#from . import views2

urlpatterns = [
    path("test1", views.index1, name="index1"),
    path("test2", views.index2, name="index2"),
    path("test3", views.index3, name="index3"),
    path("submitted", views1.index, name="index"),
    path('snippets', views.api_view_test, name='snippet-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", views.index, name="index"),
    
]
