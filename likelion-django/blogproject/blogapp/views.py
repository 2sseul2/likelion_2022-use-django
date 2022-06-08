from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# 블로그 글들을 모조리 띄우는 코드 -> 저장된 데이터들을 가져와서 보여주어야 함.
def home(request):
    posts = Blog.objects.all()
    # posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if request.method == "POST":
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form은 GET과 POST 요청 둘 다 처리가 가능한 함수
# GET: index.html에서 a태그 누를 때, 입력값을 받을 수 있는 HTML을 갖다 줘야 함
# POST: 입력한 내용을 데이터베이스에 저장해야 함. form에서 입력한 내용을 처리
def formcreate(request):
    if request.method == "POST":
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 저장
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()
    #render의 세번 째 인자: views.py 내 데이터를 html로 전달해줄 수 있는데, 딕셔너리 형태로 작성해야함.
    # 즉 form = BlogForm()에서 받은 내용을 전달해주는 것
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == "POST" or request.method == "FILES":
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm()
    #render의 세번 째 인자: views.py 내 데이터를 html로 전달해줄 수 있는데, 딕셔너리 형태로 작성해야함.
    # 즉 form = BlogForm()에서 받은 내용을 전달해주는 것
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 DB에서 가져와서
    # detail.html로 띄워주는 코드

    # pk 값을 이용해 특정 모델의 객체 한개만 가져오기. 없으면 404를 띄워라
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)
