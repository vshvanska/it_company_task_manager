from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Worker, TaskType, Position, Project, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    search_fields = ("username",)
    list_filter = ("position", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Project)
class Project(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("workers",)
    list_display = ("name", "description", "get_workers")

    def get_workers(self, obj):
        return ", ".join([worker.username for worker in obj.workers.all()])

    get_workers.short_description = "workers"


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ("name", "description",
                    "task_type", "project",
                    "deadline", "priority",
                    "get_workers")
    search_fields = ("name",)
    list_filter = ("task_type", "deadline",
                   "priority", "is_completed",
                   "project", "workers")

    def get_workers(self, obj):
        return ", ".join([worker.username for worker in obj.workers.all()])

    get_workers.short_description = "workers"
