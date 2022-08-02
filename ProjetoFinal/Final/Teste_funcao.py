from json import loads
from urllib import response

from requests import get

from .views import scrapy

# Create your tests here.


class Teste_funcao_scrapy:
    def setup(self):
        self.url = "https://www.terra.com.br"

    def Teste_de_conexao(self):
        resp = get(self.url)
        assert resp.ok

    def Teste_da_funcao(self):
        resp = get(self.url)
        resultado = scrapy(resp)
        assert resultado
