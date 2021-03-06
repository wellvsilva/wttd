from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Wellington Viana', cpf='12345678901',
                    email='wellvsilva@hotmail.com', phone='86-98852-4727')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)


    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)


    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'wellvsilva@hotmail.com']
        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = [
            'Wellington Viana',
            '12345678901',
            'wellvsilva@hotmail.com',
            '86-98852-4727',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

