from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from projects.forms import WorkerCreationForm, WorkerUpdateForm
from projects.models import Project, Task, Worker, TaskType, Position


def index(request):
    """View function for the home page of the site."""
    return render(request, "projects/index.html")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 5


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    queryset = Project.objects.prefetch_related("tasks", "tasks__workers")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10
    queryset = Task.objects.select_related("task_type", "project")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10
    queryset = Worker.objects.select_related("position")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("projects", "tasks")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    paginate_by = 20


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 20


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("projects:tasktype-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("projects:tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("projects:tasktype-list")


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("projects:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("projects:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("projects:position-list")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("projects:project-list")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("projects:worker-list")
