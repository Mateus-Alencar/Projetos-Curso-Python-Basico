import requests
import json

requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

con = json.loads(requisicao.text)

print('Dólar', con['valores']['USD']['VALOR'])
print('Euro', con['valores']['EUR']['VALOR'])
print'BTc', (con['valores']['BTC']['VALOR'])