from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
# media 파일 다루기 위한 import, 암기하는게 좋겠다.라 말함.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용해 Blog 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용해 Blog 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform을 이용해 Blog 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # detail/1, 2,
    # detail 함수에 넘길 값: <int 형> blog_id 의 변수명으로..
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
]
# media 파일에 접근하기 위한 url 추가, 암기하는게 좋다라고 말함.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
