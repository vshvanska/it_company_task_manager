import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from projects.models import Position, Project, Task, TaskType


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Test")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
            position=self.position
        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="admin123",
            position=self.position
        )
        self.project = Project.objects.create(
            name="Test Project",
            description="Test Description",
        )
        self.project.workers.set([self.worker])
        self.task_type = TaskType.objects.create(
            name="test type"
        )
        self.task = Task.objects.create(
            name="Test task",
            description="Test Description",
            deadline=datetime.datetime.now(),
            priority="middle",
            task_type=self.task_type,
            project=self.project,
        )
        self.task.workers.set([self.worker])

    def test_worker_position_listed(self):
        url = reverse("admin:projects_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:projects_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_add_worker_detail_position_listed(self):
        url = reverse("admin:projects_worker_add")
        response = self.client.get(url)
        self.assertTrue(response, self.worker.position)

    def test_get_workers_displayed_in_project_admin(self):
        url = reverse("admin:projects_project_change", args=[self.project.id])
        response = self.client.get(url)
        self.assertContains(response, self.project.workers.first().username)

    def test_get_workers_displayed_in_task_admin(self):
        url = reverse("admin:projects_task_change", args=[self.task.id])
        response = self.client.get(url)
        self.assertContains(response, self.task.workers.first().username)
