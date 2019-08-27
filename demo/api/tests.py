import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from celery.result import AsyncResult
from api.models import Result


class ResultCeleryTests(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_2_2_task(self):

        url = reverse('test-list')
        data = {'x': 2, 'y': 2}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data.get('id')
        result = Result.objects.get(pk=pk)
        task = AsyncResult(result.task_id)

        output = task.get()

        self.assertEqual(Result.objects.get(pk=pk).output, data['x']+data['y'])
        self.assertEqual(Result.objects.get(pk=pk).output, output)

    def test_add_4_12_task(self):

        url = reverse('test-list')
        data = {'x': 4, 'y': 12}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data.get('id')
        result = Result.objects.get(pk=pk)
        task = AsyncResult(result.task_id)

        output = task.get()

        self.assertEqual(Result.objects.get(pk=pk).output, data['x']+data['y'])
        self.assertEqual(Result.objects.get(pk=pk).output, output)


