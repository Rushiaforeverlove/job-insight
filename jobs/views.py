from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Favorite

from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# 首頁
def home(request):

    jobs = Job.objects.all().order_by('-id')

    return render(request, 'jobs/home.html', {
        'jobs': jobs
    })


# 詳細頁
def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    return render(request, 'jobs/detail.html', {
        'job': job
    })


# 收藏功能
def toggle_favorite(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    favorite = Favorite.objects.filter(
        user=request.user,
        job=job
    )

    if favorite.exists():

        favorite.delete()

        return JsonResponse({
            'status': 'removed'
        })

    Favorite.objects.create(
        user=request.user,
        job=job
    )

    return JsonResponse({
        'status': 'added'
    })


# 收藏頁
def favorites(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    return render(request, 'jobs/favorites.html', {
        'favorites': favorites
    })


# 註冊
def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():

            return render(request, "jobs/register.html", {
                "error": "使用者已存在"
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('/')

    return render(request, "jobs/register.html")


# 登入
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

        return render(request, "jobs/login.html", {
            "error": "帳號或密碼錯誤"
        })

    return render(request, "jobs/login.html")


# 登出
def logout_view(request):

    logout(request)

    return redirect('/')