from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectMembership, Task


@login_required(login_url='users/login')
def index(request):
    user = request.user
    result_project_membership = ProjectMembership.objects.filter(member_id=user.id)
    result_projects = []
    for projects in result_project_membership:
        temp = Project.objects.get(id=projects.project_id)
        result_projects.append(temp)
    result_projects.sort(key=lambda x: x.updated_at, reverse=True)
    result_task_list = Task.objects.filter(assigned_id=user.id).order_by('due_date')[:5]
    return render(request, 'projects/index.html', {'projects': result_projects, 'tasks':result_task_list})