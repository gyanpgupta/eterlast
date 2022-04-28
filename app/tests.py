import json
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Collection
from rest_framework import status
from rest_framework.test import APITestCase

class APITest(APITestCase):

    def setUp(self):
        self.auth_user = User.objects.create(
            username="test121", password="Tes@t123")
        self.valid_url = reverse('create-mint')
        self.invalid_url = 'create-minte'
    
        self.collection = Collection.objects.create(
            creator=self.auth_user,
            name="Testing"
        )
    def test_valid_url(self):
        # Make request
        response = self.client.get(self.valid_url)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_url(self):
        # Make request
        response = self.client.get(self.invalid_url)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_invalid_data(self):
        data = {
            "name": "Demo",
            "collection": 4
        }
        # Make request
        response = self.client.post(self.valid_url, data)
        # Check status response
        self.assertEqual(response.status_code, 400)
    
    def test_valid_data(self):
        data = {
            "name": "Demo",
            "collection": self.collection.pk
        }
        # Make request
        response = self.client.post(self.valid_url, data)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @classmethod
    def tearDownClass(self):
        pass
