"""
URL configuration for Try project.

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
from django.contrib import admin
from django.urls import path, include
from hi.views import welcome,create_user,login_view,hi,my_question
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('user/',create_user,name='create_user'),
    path('login/', login_view, name='login1'),  
    path('login/success.html/',hi,name='success'),
    path('ques/',my_question)
]
