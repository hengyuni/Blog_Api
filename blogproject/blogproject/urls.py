"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from blogs.views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)#register "/blogs" routes
# /blogs/ get show us all todos in json
# /blogs/ post create a new todo and accept json
# /blogs/<id> get show us one individial todo
# /blogs/<id> put update in individual todo
# /blogs/<id> delete an individual today

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
