import unittest
from django.test import Client
import json




class BasicTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()


    def test_get_trasacao(self):
        response = self.client.get('/api/v1/transacao/estabelecimento',{'cnpj':'45.283.163/0001-67'})
        self.assertEqual(response.status_code, 200)

    def test_post_trasacao(self):
        response = self.client.post('/api/v1/transacao',{"estabelecimento": "45.283.163/0001-67","cliente": "094.214.930-01","valor": 590.01,"descricao": "Almoço em restaurante chique pago via Shipay!"},content_type="application/json")

        self.assertEqual(response.status_code, 200)