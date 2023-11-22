import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from projects.forms import TaskCreateForm, TaskUpdateForm
from projects.models import Task, Position, TaskType, Project
from projects.tests.test_view import TASK_URL, PROJECT_URL


class FormsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="test_position")
        self.task_type = TaskType.objects.create(name="test_type")
        self.user = get_user_model().objects.create_superuser(
            username="test1",
            password="password123",
            position=self.position
        )
        self.worker = get_user_model().objects.create_superuser(
            username="test2",
            password="password123",
            position=self.position
        )
        self.project = Project.objects.create(name="test",
                                              description="description")
        self.client.force_login(self.user)

    def test_task_form_with_deadline_in_future(self):
        form_data = {
            "name": "taskname",
            "description": "taskdescription",
            "deadline": timezone.now() + datetime.timedelta(days=3),
            "priority": "urgent",
            "task_type": self.task_type,
            "project": self.project,
            "workers": [self.user, self.worker]
        }
        form = TaskCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        form = TaskUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_with_deadline_in_past(self):
        form_data = {
            "name": "taskname",
            "description": "taskdescription",
            "deadline": timezone.now() - datetime.timedelta(days=3),
            "priority": "urgent",
            "task_type": self.task_type,
            "project": self.project,
            "workers": [self.user, self.worker]
        }
        form = TaskCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        form = TaskUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_with_deadline_in_now(self):
        form_data = {
            "name": "taskname",
            "description": "taskdescription",
            "deadline": timezone.now(),
            "priority": "urgent",
            "task_type": self.task_type,
            "project": self.project,
            "workers": [self.user, self.worker]
        }
        form = TaskCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        form = TaskUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_search_by_name(self):
        self.task1 = Task.objects.create(
            name="taskname",
            description="taskdescription",
            deadline=timezone.now(),
            priority="urgent",
            task_type=self.task_type,
            project=self.project,
        )
        self.task1 = Task.objects.create(
            name="tsknme",
            description="taskdescription",
            deadline=timezone.now(),
            priority="urgent",
            task_type=self.task_type,
            project=self.project,
        )

        response = self.client.get(TASK_URL, {"name": "a"})
        tasks = Task.objects.filter(name__icontains="a")
        self.assertEqual(list(response.context["task_list"]), list(tasks))

    def test_project_search_by_name(self):
        self.project1 = Project.objects.create(
            name="test2",
            description="description"
        )
        self.project3 = Project.objects.create(
            name="project",
            description="description"
        )

        response = self.client.get(PROJECT_URL, {"name": "test"})
        projects = Project.objects.filter(name__icontains="test")
        self.assertEqual(list(response.context["project_list"]),
                         list(projects))
