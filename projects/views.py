from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task, User, Comment


@login_required()
def index(request):
    user = request.user
    result_projects = Project.objects.filter(projectmembership__member_id=user.id).order_by('title')[:10]
    result_task_list = Task.objects.filter(assigned_id=user.id).order_by('due_date')[:5]
    return render(request, 'projects/index.html', {'projects': result_projects, 'tasks':result_task_list})


@login_required()
def project_page(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    task_list = Task.objects.filter(project__id=project_id)
    members_list = User.objects.filter(projectmembership__project_id=project.id)
    return render(request, 'projects/project_page.html', {'task_list': task_list, 'members_list': members_list})


@login_required()
def task_page(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    comment_list = Comment.objects.filter(task__id=task.id)
    return render(request, 'projects/task_page.html', {'comment_list': comment_list, 'task': task})

