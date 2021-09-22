import requests
import json
from unidecode import unidecode

urlEstados = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

estados = requests.get(urlEstados)
estados = estados.json()

finalEstados = []


def getUrlCidades(uf):
  return 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + uf + '/municipios'


for estado in estados:
  municipios = requests.get(getUrlCidades(estado['sigla']))
  municipios = municipios.json()

  finalMunicipios = []
  for municipio in municipios:
    finalMunicipios.append({
      'codigo': str(municipio['id']),
      'nome': unidecode(municipio['nome']).upper()
    })

  finalEstados.append({
    'codigo': str(estado['id']),
    'sigla': estado['sigla'],
    'nome': unidecode(estado['nome']).upper(),
    'municipios': finalMunicipios
  })


with open('estados_municipios_brasil_2021.json', 'w', encoding='utf8') as f:
  f.write(json.dumps(finalEstados))
input('Arquivo criado com sucesso!')