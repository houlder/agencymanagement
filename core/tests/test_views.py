from django.test import TestCase


class CoreViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        pass

    def test_view_url_exists_at_desired_location(self):
        """Access to homepage"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
