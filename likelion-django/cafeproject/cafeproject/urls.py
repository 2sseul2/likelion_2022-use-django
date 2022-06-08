from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail', views.detail, name='detail'),
    # detail 1~9 까지 일일이 만들어줘야함 -> Model 사용한다.
]
