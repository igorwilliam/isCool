from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

# class NewTopicViewTestCase(TestCase):
#
#     def setup(self):
#         self.client = Client()
#         self.url = reverse('post')
#
#     def test_newTopic(self):
#         data = {'title': '','content': ''}
#         response = self.client.post(self.url,data)
#         self.assertFormError(response, 'form', 'title', 'Este campo é obrigátorio')
#         self.assertFormError(response, 'form', 'content', 'Este campo é obrigátorio')
#
#
