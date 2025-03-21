from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import KPI, AssetKPI

# Create your tests here.
class KPITests(APITestCase):
    def test_create_kpi(self):
        url = reverse('kpi_list_create')  # The name of the URL in urls.py
        data = {
            "name": "Test KPI",
            "expression": "ATTR + 10",
            "description": "This is a test KPI"
        }
        response = self.client.post(url, data, format='json')

        # Check if the response has a 201 CREATED status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Test KPI")
        self.assertEqual(response.data['expression'], "ATTR + 10")

        # Verify the KPI was actually created in the database
        self.assertEqual(KPI.objects.count(), 1)
        self.assertEqual(KPI.objects.get().name, "Test KPI")
    def test_list_kpis(self):
        # First create some KPI instances
        KPI.objects.create(name="KPI 1", expression="ATTR + 20")
        KPI.objects.create(name="KPI 2", expression="ATTR / 5")

        url = reverse('kpi_list_create')
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if two KPIs are returned
        self.assertEqual(response.data[0]['name'], "KPI 1")
        self.assertEqual(response.data[1]['name'], "KPI 2")
    def test_link_asset_to_kpi(self):
        # Create a KPI first
        kpi = KPI.objects.create(name="KPI for Asset", expression="ATTR - 5")

        url = reverse('link_asset_to_kpi')
        data = {
            "asset_id": "1",
            "kpi": kpi.id
        }
        response = self.client.post(url, data, format='json')

        # Check if the response has a 201 CREATED status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['asset_id'], "1")
        self.assertEqual(response.data['kpi'], kpi.id)

        # Verify the AssetKPI was created in the database
        self.assertEqual(AssetKPI.objects.count(), 1)
        self.assertEqual(AssetKPI.objects.get().asset_id, "1")
