from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .models import Task

class TaskTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="john", email="foo@bar.com")
        cls.user.set_password("password123")
        cls.user.save()
        cls.token = Token.objects.create(user=cls.user)
        cls.task = Task.objects.create(
            name="My Task", description="My task description", user=cls.user, priority=1, completed=False
        )

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.token.delete()
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        self.client.force_authenticate(user=self.user, token=self.token)

    def test_get_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_get_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.task.name)

    def test_create_task(self):
        url = reverse("task-list")
        data = {
            "name": "New Task",
            "description": "New task description",
            "priority": 2,
            "completed": False
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), data["name"])

    def test_update_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        data = {
            "name": "Updated Task",
            "description": "Updated task description",
            "priority": 3,
            "completed": True
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), data["name"])
        self.assertTrue(response.data.get("completed"))

    def test_partial_update_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        data = {
            "completed": True
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("completed"))

    def test_delete_task(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_filter_tasks_by_completed(self):
        url = reverse("task-list")
        response = self.client.get(url, {'completed': False}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertFalse(response.data.get("results")[0].get("completed"))
