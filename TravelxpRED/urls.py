"""TravelxpRED URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path


from django.urls import include
from django.conf import settings

from AdminManagement import views as admin_views
from CommentManagement import views as comment_views
from PostManagement import views as post_views


urlpatterns = [
    path('admin/', admin.site.urls),


    path('adminlist/', admin_views.showAdmin, name='Admin'),
    path('user/', user_views.showUser, name='User'),
    path('insertuser/', user_views.insertUser, name='insertUser'),
    path('registration/', user_views.registration, name='registration'),
    path('comment/', comment_views.showComment, name='Comment'),
    path('post/', post_views.showPost, name='Post'),
    path('accounts/', include('django.contrib.auth.urls'))

]
