from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm


# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj
    }
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()

    context = {
        'job_detail': job_detail,
        'form': form
    }
    return render(request, 'job/job_detail.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()
    return render(request, 'job/add_job.html', {'form': form})
