from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position,
                                 on_delete=models.PROTECT,
                                 related_name="workers")

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField()
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="projects")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("urgent", "Urgent"),
        ("high", "High"),
        ("middle", "Middle"),
        ("low", "Low"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20,
                                choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType,
                                  on_delete=models.PROTECT,
                                  related_name="tasks")
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="tasks")
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="tasks")

    class Meta:
        ordering = ("deadline", "priority")

    def __str__(self):
        return self.name
