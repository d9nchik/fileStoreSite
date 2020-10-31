"""fileStoreSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from myfiles.views import upload_file, get_file, MyLoginView, get_links

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_file),
    path('links/', get_links),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    re_path('(?P<file_unique>[\\da-f]{5})/?', get_file),
    #     User.objects.create_user(username='usual_user', email='user@example.com', password='NotSecRetAtAll')
]
