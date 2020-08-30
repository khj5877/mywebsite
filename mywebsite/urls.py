"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")), #blog 주소를 치고 들어오면 그것을 블로그 앱이 처리하게 해줘라
    path("", RedirectView.as_view(url="/blog/",permanent=True)), #아무것도 없이 들어오면 블로그로 넘겨줘라

] 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #javascript 이미지 파일들을 처리할수 있도록 해주는 세팅
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #javascript 이미지 파일들을 처리할수 있도록 해주는 세팅
