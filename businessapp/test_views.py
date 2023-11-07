import json
from django.test import TestCase, Client
from .models import Business


class BusinessTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_business(self):
        data = {
            'name': 'Test Business',
            'address': 'Test Address',
            'owner_info': 'Test Owner',
            'employee_size': 10
        }
        response = self.client.post('/myapp/perform_operation/create/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Business.objects.count(), 1)
        self.assertEqual(Business.objects.get().name, 'Test Business')

    def test_update_business(self):
        business = Business.objects.create(
            name='Original Business',
            address='Original Address',
            owner_info='Original Owner',
            employee_size=5
        )
        data = {
            'name': 'Updated Business',
            'address': 'Updated Address',
            'owner_info': 'Updated Owner',
            'employee_size': 8
        }
        response = self.client.post(f'/myapp/perform_operation/update/{business.id}/', data)
        self.assertEqual(response.status_code, 200)
        updated_business = Business.objects.get(id=business.id)
        self.assertEqual(updated_business.name, 'Updated Business')
        self.assertEqual(updated_business.employee_size, 8)

    # Add more test cases for other operations

