import requests
import locale
import tabulate
from bs4 import BeautifulSoup
from modelos import Acoes, Estrategia

#Tratamento dos numeros
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def trata_porcentagem(porcentagem_str):
    return  locale.atof(porcentagem_str.split('%')[0])

def trata_decimal(decimal_str):
    return locale.atof(decimal_str)

#Lista com todos os fundos filtrados
resultado  = []

#Estratégia de investimento definida de forma abritária
estrategia = Estrategia(
    p_l_maximo=10,
    div_yield_minimo=5,
    roic_minimo=10,
    roe_minimo=10
)


#Coleta dos Dados
headers = {'User-agent':'Mozilla/5.0'}
r = requests.get('https://www.fundamentus.com.br/resultado.php', headers=headers)

soup = BeautifulSoup(r.text,'html.parser')

linhas = soup.find(id="resultado").find('tbody').find_all('tr')

for linha in linhas:
    dados_acao = linha.find_all('td')
    papel = dados_acao[0].text
    cotacao = trata_decimal(dados_acao[1].text)
    p_l = trata_decimal(dados_acao[2].text)
    p_vp = trata_decimal(dados_acao[3].text)
    div_yield = trata_porcentagem(dados_acao[5].text)
    roic = trata_porcentagem(dados_acao[15].text)
    roe = trata_porcentagem(dados_acao[16].text)

    acao = Acoes(papel, cotacao, p_l, p_vp, div_yield, roic, roe)

    if estrategia.aplicar_estrategia(acao):
        resultado.append(acao)


#Esqueleto da tabela
cabecalho = ['PAPEL', 'COTAÇÃO', 'P/L', 'DIVIDEND YIELD', 'ROE']
tabela = []

for elemento in resultado:
    tabela.append([
        elemento.papel,
        locale.currency(elemento.cotacao),
        elemento.p_l,
        f'{locale.str(elemento.div_yield)} %',
        f'{locale.str(elemento.roe)} %'
    ])

print(tabulate.tabulate(tabela, headers=cabecalho,showindex='always', tablefmt='fancy_grid'))
