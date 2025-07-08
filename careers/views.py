from django.shortcuts import render, get_object_or_404
from .models import Job
from django.http import JsonResponse
from django.db.models import Q

def home(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'home.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})
def search_jobs(request):
    q = request.GET.get('q', '')
    if q:
        jobs = Job.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(company__icontains=q)
        )
    else:
        jobs = Job.objects.all()

    data = list(jobs.values('title', 'company', 'location', 'description', 'posted_at'))
    return JsonResponse(data, safe=False)
