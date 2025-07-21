from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('', lambda request: HttpResponse("📢 Django 서버가 잘 작동 중입니다!")),
    path('admin/', admin.site.urls),
    path('api/', include('post.urls')), 
]