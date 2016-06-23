from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from model_mommy import mommy
from modules.board.models import Job


class HomeTest(TestCase):
    '''
        Tests of board home view
    '''
    def setUp(self):
        self.job = mommy.make(Job, title='Vaga de estágio')
        self.response_home = self.client.get(reverse('home'))
        self.cliente = Client()

    def test_home_response_200(self):
        self.assertEqual(self.response_home.status_code, 200)

    def test_home_context_with_one_job(self):
        self.assertEqual(len(self.response_home.context['jobs']), 1)


class JobTest(TestCase):
    '''
        Tests of board models
    '''
    def setUp(self):
        self.job = mommy.make(Job, title='Vaga de estágio')

    def test_create_job(self):
        self.assertEqual(self.job.__str__(), 'Vaga de estágio')
