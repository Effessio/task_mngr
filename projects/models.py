# -*- coding: utf-8 -*-
from django.db import models
from users.models import User


class Project(models.Model):

    title = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)
    is_public = models.BooleanField(default=False)
    members = models.ManyToManyField(User, through='ProjectMembership')

    def __unicode__(self):
        return self.title


class ProjectMembership(models.Model):

    class PROJECT_ROLE(object):
        MANAGER = 1
        DEVELOPER = 2
        TESTER = 3
        AUDITOR = 4

        ALL = (
            (MANAGER, 'Manager'),
            (DEVELOPER, 'Developer'),
            (TESTER, 'Tester'),
            (AUDITOR, 'Auditor'),
        )
    member = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.IntegerField(choices=PROJECT_ROLE.ALL)

    def __unicode__(self):
        return u'{0} is {1} of {2}'.format(self.member, self.role, self.project)


class Task(models.Model):

    class TASK_TYPE(object):
        BUG = 1
        FEATURE = 2
        TASK = 3
        CONTAINER = 4

        ALL = (
            (BUG, 'Bug'),
            (FEATURE, 'Feature'),
            (TASK, 'Task'),
            (CONTAINER, 'Container'),
        )

    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)
    due_date = models.DateTimeField('due date')
    reporter = models.ForeignKey(User, related_name="reported_tasks")
    assigned = models.ForeignKey(User, related_name="assigned_tasks")
    task_type = models.IntegerField(choices=TASK_TYPE.ALL)
    parent_task = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    text = models.TextField()

    def __unicode__(self):
        return self.text
