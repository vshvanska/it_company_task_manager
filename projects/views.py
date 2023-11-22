from django.shortcuts import render
from django.views import generic

from projects.models import Project, Task


def index(request):
    """View function for the home page of the site."""
    return render(request, "projects/index.html")


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 5


class ProjectDetailView(generic.DetailView):
    model = Project
    queryset = Project.objects.prefetch_related("tasks", "tasks__workers")


class TaskListView(generic.ListView):
    model = Project
    paginate_by = 10
    queryset = Task.objects.select_related("task_type", "project")


class TaskDetailView(generic.DetailView):
    model = Task