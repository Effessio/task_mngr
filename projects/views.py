from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, Task, User, Comment


@login_required()
def index(request):
    user = request.user
    projects = Project.objects.filter(projectmembership__member_id=user.id).order_by('title')
    paginator = Paginator(projects, 5)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    task_list = Task.objects.filter(assigned_id=user.id).order_by('due_date')[:5]
    return render(request, 'projects/index.html', {'projects': projects, 'tasks': task_list})


@login_required()
def project_page(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    task_list = Task.objects.filter(project__id=project_id)
    paginator = Paginator(task_list, 5)
    page = request.GET.get('page')
    try:
        task_list = paginator.page(page)
    except PageNotAnInteger:
        task_list = paginator.page(1)
    except EmptyPage:
        task_list = paginator.page(paginator.num_pages)
    members_list = User.objects.filter(projectmembership__project_id=project.id)
    return render(request, 'projects/project_page.html', {'task_list': task_list, 'members_list': members_list})


@login_required()
def task_page(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    comment_list = Comment.objects.filter(task__id=task.id)
    return render(request, 'projects/task_page.html', {'comment_list': comment_list, 'task': task})

