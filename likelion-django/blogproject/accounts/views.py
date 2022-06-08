from django.shortcuts import render, redirect
# 로그인, 아웃 기능 수행
from django.contrib import auth
# 장고는 유저 기능이 원래 있다.
from django.contrib.auth.models import User


def login(request):
    # POST: 로그인 처리
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # 실제 db에 등록되어 있는지를 확인해줌.
        # 있다면, 그 회원 객체를 반환, 아니면 none을 반환
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            # 로그인 해줌.
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET: login.html 띄워줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
