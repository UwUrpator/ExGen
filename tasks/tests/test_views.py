from django.test import TestCase

from users.models import EmailUser


class TestCreateTask(TestCase):

    def setUp(self):
        self.client.force_login(EmailUser.objects.create(email='test@email.com'))

    def test_create_task_page_anonymous(self):
        self.client.logout()
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_task_page_logged(self):
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_task_context(self):
        context = self.client.get('/tasks/create/').context
        self.assertTrue('task' in context)
        self.assertTrue('variables' in context)
