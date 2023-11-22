import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from projects.models import Project, Task, Position, TaskType

PROJECT_URL = reverse("projects:project-list")
WORKER_URL = reverse("projects:worker-list")
TASK_URL = reverse("projects:task-list")


class PublicProjectTest(TestCase):
    def test_login_required(self):
        res = self.client.get(PROJECT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateProjectTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="test position")
        self.user1 = get_user_model().objects.create_user(
            username="test",
            password="test321",
            position=self.position
        )
        self.client.force_login(self.user1)

    def test_retrieve_project(self):
        Project.objects.create(name="test_project1",
                               description="description",)
        Project.objects.create(name="test_project2",
                                    description="description",)
        response = self.client.get(PROJECT_URL)
        self.assertEqual(response.status_code, 200)
        projects = Project.objects.all()
        self.assertEqual(list(response.context["project_list"]),
                         list(projects))
        self.assertTemplateUsed(response, "projects/project_list.html")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="test position")
        self.user1 = get_user_model().objects.create_user(
            username="test",
            password="test321",
            position=self.position
        )
        self.client.force_login(self.user1)

    def test_retrieve_worker(self):
        get_user_model().objects.create(
            username="driver1",
            password="driver123",
            position=self.position
        )
        get_user_model().objects.create(
            username="driver2",
            password="driver123",
            position=self.position
        )
        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)
        workers = get_user_model().objects.all()
        self.assertEqual(list(response.context["worker_list"]),
                         list(workers))
        self.assertTemplateUsed(response, "projects/worker_list.html")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="test position")
        self.user1 = get_user_model().objects.create_user(
            username="test",
            password="test321",
            position=self.position
        )
        self.client.force_login(self.user1)

    def test_retrieve_task(self):
        project = Project.objects.create(name="test_project1",
                                         description="description")
        task_type = TaskType.objects.create(name="testtype")
        Task.objects.create(
            name="test_task",
            description="test_description",
            deadline=datetime.datetime.now(),
            priority="low",
            task_type=task_type,
            project=project,
        )
        Task.objects.create(
            name="test_task2",
            description="test_description2",
            deadline=datetime.datetime.now(),
            priority="low",
            task_type=task_type,
            project=project,
        )
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "projects/task_list.html")
