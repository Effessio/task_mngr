from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from projects.models import Project, ProjectMembership, Task


@login_required(login_url='users/login')
def index(request):
    user = request.user
    a = ProjectMembership.objects.filter(member_id=user.id)
    result_projects = []
    for projects in a:
        proj = Project.objects.get(id=projects.project_id)
        result_projects.append(proj)
    result_projects.sort(key=lambda x: x.updated_at, reverse=True)
    result_task_list = Task.objects.filter(assigned_id=user.id).order_by('due_date')[:5]
    #task_list_for_user.sort(key=lambda x: x.due_date)
    #result_task = task_list_for_user[0:4]
    return render(request, 'projects/index.html', {'projects': result_projects, 'tasks':result_task_list})