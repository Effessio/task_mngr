# -*- coding: utf-8 -*-
from django.contrib import admin
from projects.models import *


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'is_public']

class TaskAdmin(admin.ModelAdmin):
    fields = ['project', 'title', 'description', 'due_date', 'reporter', 'assigned', 'task_type', 'parent_task']


class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'task', 'text']


class ProjectMembershipAdmin(admin.ModelAdmin):
    fields = ['member', 'project', 'role']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ProjectMembership, ProjectMembershipAdmin)





