
import re

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests import get


def scrapy(url):
    # processo 1
    lista_fixa = []
    links = []
    resposta = requests.get(url)
    tag = BeautifulSoup(resposta.text, "html.parser")
    Linkspagina = tag.find_all('a', href=True, limit=10)
    for link in Linkspagina:
        links.append(link['href'])

    # tratando os links do primeiro processo processo com regex
    for link in links:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(link)):
            lista_fixa.append(link)

    # processo 2
    for links_processo2 in lista_fixa:
        lista_processo2 = []
        processo2 = requests.get(links_processo2)
        tag_processo2 = BeautifulSoup(processo2.text, "html.parser")
        link_processo2 = tag_processo2.find_all('a', href=True, limit=5)
        for processo_2 in link_processo2:
            lista_processo2.append(processo_2['href'])

    # tratando os links do segundo processo com regex
    for processo_2 in lista_processo2:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(processo_2)):
            lista_fixa.append(processo_2)

    # Processo 3
    for links_processo3 in lista_fixa:
        lista_processo3 = []
        processo3 = requests.get(links_processo3)
        tag_processo3 = BeautifulSoup(processo3.text, "html.parser")
        link_processo3 = tag_processo3.find_all('a', href=True, limit=5)
        for processo_3 in link_processo3:
            lista_processo3.append(processo_3['href'])

    # tratando os links do terceiro processo com regex
    for processo_3 in lista_processo3:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(processo_3)):
            lista_fixa.append(processo_3)

    # Processo 4
    for links_processo4 in lista_fixa:
        lista_processo4 = []
        processo4 = requests.get(links_processo4)
        tag_processo4 = BeautifulSoup(processo4.text, "html.parser")
        link_processo4 = tag_processo4.find_all('a', href=True, limit=5)
        for processo_4 in link_processo4:
            lista_processo4.append(processo_4['href'])

    # tratando os links do quarto processo com regex
    for processo_4 in lista_processo4:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(processo_4)):
            lista_fixa.append(processo_4)

    # processo 5
    for links_processo5 in lista_fixa:
        lista_processo5 = []
        processo5 = requests.get(links_processo5)
        tag_processo5 = BeautifulSoup(processo5.text, "html.parser")
        link_processo5 = tag_processo5.find_all('a', href=True, limit=5)
        for processo_5 in link_processo5:
            lista_processo5.append(processo_5['href'])

    # tratando os links do terceiro processo com regex
    for processo_5 in lista_processo5:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(processo_5)):
            lista_fixa.append(processo_5)

    # retirando links repetidos
    lista_nova = []
    lista_sem_repeticoes = list(set(lista_fixa))
    for lista_sem in lista_sem_repeticoes:
        lista_nova.append(lista_sem)

    return lista_nova


# controlado do forms


def homepage(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get('url', None)
        link = scrapy(url)
        context['link'] = link
    return render(request, 'home.html', context=context
                  )
