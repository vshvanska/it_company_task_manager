"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from projects.views import (index,
                            ProjectListView,
                            ProjectDetailView,
                            TaskListView,
                            TaskDetailView,
                            WorkerListView,
                            WorkerDetailView,
                            TaskTypeListView,
                            PositionListView,
                            TaskTypeCreateView,
                            PositionCreateView,
                            TaskTypeUpdateView,
                            PositionUpdateView,
                            TaskTypeDeleteView,
                            PositionDeleteView,
                            ProjectCreateView,
                            ProjectUpdateView,
                            ProjectDeleteView,
                            WorkerCreateView,
                            WorkerUpdateView,
                            WorkerDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path(
        "projects/",
        ProjectListView.as_view(),
        name="project-list"),
    path("projects/<int:pk>/",
         ProjectDetailView.as_view(),
         name="project-detail"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/",
         WorkerDetailView.as_view(),
         name="worker-detail"),
    path("tasks/tasktypes/",
         TaskTypeListView.as_view(),
         name="tasktype-list"),
    path("tasks/tasktypes/create/",
         TaskTypeCreateView.as_view(),
         name="tasktype-create"),
    path("tasks/tasktypes/update/<int:pk>",
         TaskTypeUpdateView.as_view(),
         name="tasktype-update"),
    path("tasks/tasktypes/delete/<int:pk>",
         TaskTypeDeleteView.as_view(),
         name="tasktype-delete"),
    path("workers/positions/",
         PositionListView.as_view(),
         name="position-list"),
    path("workers/positions/create/",
         PositionCreateView.as_view(),
         name="position-create"),
    path("workers/positions/update/<int:pk>",
         PositionUpdateView.as_view(),
         name="position-update"),
    path("workers/positions/delete/<int:pk>",
         PositionDeleteView.as_view(),
         name="position-delete"),
    path("projects/create/",
         ProjectCreateView.as_view(),
         name="project-create"),
    path("projects/update/<int:pk>",
         ProjectUpdateView.as_view(),
         name="project-update"),
    path("projects/delete/<int:pk>",
         ProjectDeleteView.as_view(),
         name="project-delete"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/",
         WorkerUpdateView.as_view(),
         name="worker-update"),
    path("workers/<int:pk>/delete/",
         WorkerDeleteView.as_view(),
         name="worker-delete"),

]

app_name = "projects"
