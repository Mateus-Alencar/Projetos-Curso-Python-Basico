import re
import requests

requis = requests.get('https://loucosporcoxinha.com.br/contato/')

padrao = re.findall(r'[\w\.-] +@ [\w-] =+\. [\w\.-] +', requis.text)

if padrao:
  print(padrao)
else:
  print('padrão não encontrado')