from django.shortcuts import render, get_object_or_404
from .models import Job
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