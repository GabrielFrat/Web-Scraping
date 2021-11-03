import requests
import pandas as pd
import json


def busca_atacadao(tipo):
    url = 'https://www.atacadao.com.br/catalogo/search/?q=&category_id=' \
          'null&category[]={}&page=2&order_by=-relevance'.format(tipo)
    r = requests.get(url)
    with open('dados_atacadao.json', 'w') as arq:
        arq.write(str(r.text))


busca_atacadao('bebidas')


def exporta_excel():
    with open('dados_atacadao.json') as file_json:
        read_content = json.load(file_json)
        results = read_content['results']

    pd_dataFrame = pd.DataFrame(results)
    pd_dataFrame = pd_dataFrame.filter(items=['name', 'brand', 'type'])
    print(pd_dataFrame)
    pd_dataFrame.to_excel(r'C:\Users\gabri\PycharmProjects\DadosAtacadao\atacadao_data.xlsx')


exporta_excel()


