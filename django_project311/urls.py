"""django_project311 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url

urlpatterns = [
   path('admin/', admin.site.urls),
   # # path('', include('blog.urls')),
     # path('', include('TASKSSS.urls')),
   #  # path('index/', include('TASKSSS.urls')),
     # path('add/', include('TASKSSS.urls')),
     # path('res/',include('TASKSSS.urls')),
    # path('show/',include('TASKSSS.urls')),
    path('',include('NGO.urls')),
    path('donation',include('NGO.urls')),
    path('payment/',include('NGO.urls')),
    path('acknwl/',include('NGO.urls')),
    # path('sup/',include('NGO.urls')),
    # path('login/',user_view.Login),
    # path('logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'), 
    # path('register/', user_view.register, name ='register'), 
]

