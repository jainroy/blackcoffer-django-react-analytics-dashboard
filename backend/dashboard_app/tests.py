from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import InsightEntry


class InsightEntryAPITest(TestCase):
    def setUp(self):
        # Create a simple entry for testing
        InsightEntry.objects.create(
            title='Test entry',
            intensity=5,
            likelihood=3,
            relevance=4,
        )
        self.client = APIClient()

    def test_entries_list_returns_records(self):
        url = reverse('entries-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data['count'], 1)
