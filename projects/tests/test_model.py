import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from projects.models import TaskType, Position, Project, Task


class ModelsTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="test_tasktype")
        self.position = Position.objects.create(name="test_position")
        self.worker1 = get_user_model().objects.create(
            username="capsparrow",
            password="test123456",
            first_name="Jack",
            last_name="Sparrow",
            position=self.position
        )
        self.worker2 = get_user_model().objects.create(
            username="testworker",
            password="test123456",
            first_name="Test",
            last_name="Worker",
            position=self.position
        )
        self.project = Project.objects.create(name="test_project",
                                              description="description",)
        self.task = Task.objects.create(
            name="test_task",
            description="test_description",
            deadline=datetime.datetime.now(),
            priority="low",
            task_type=self.task_type,
            project=self.project,
        )

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "test_tasktype")

    def test_position_str(self):
        self.assertEqual(str(self.position), "test_position")

    def test_worker_str(self):
        self.assertEqual(str(self.worker1), "capsparrow (Jack Sparrow)")

    def test_project_str(self):
        self.assertEqual(str(self.project), "test_project")

    def test_task_str(self):
        self.assertEqual(str(self.task), "test_task")
