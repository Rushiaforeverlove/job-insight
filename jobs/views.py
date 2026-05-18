from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Job, Favorite
from django.core.paginator import Paginator


def home(request):

    keyword = request.GET.get('keyword')

    if keyword:
        job_list = Job.objects.filter(title__icontains=keyword)
    else:
        job_list = Job.objects.all()

    paginator = Paginator(job_list, 6)  # 每頁6筆

    page_number = request.GET.get('page')

    jobs = paginator.get_page(page_number)

    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    return render(request, 'jobs/detail.html', {'job': job})

def favorites(request):

    if not request.user.is_authenticated:
        return redirect('/login')

    favs = Favorite.objects.filter(user=request.user)

    return render(request, 'jobs/favorites.html', {
        "favs": favs
    })

def toggle_favorite(request, job_id):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "not login"}, status=403)

    job = Job.objects.get(id=job_id)

    fav, created = Favorite.objects.get_or_create(
        user=request.user,
        job=job
    )

    if not created:
        fav.delete()
        return JsonResponse({"status": "removed"})

    return JsonResponse({"status": "added"})