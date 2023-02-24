import json

# Abre o arquivo JSON para leitura
with open('geojs-100-mun.json', 'rb') as f:
    # Carrega o conteúdo do arquivo em um objeto Python
    dados = json.load(f)

# remove o que não for sul do pais
t = {'type': 'FeatureCollection', 'features': [{'geometry': {'type': 'Point', 'coordinates': [113.5546875, 63.704722429433225]}, 'type': 'Feature', 'properties': {'city': 'city1'}}, {'geometry': {'type': 'Polygon', 'coordinates': [0, 0]}, 'type': 'Feature', 'properties': {'id': '', 'name': '', 'description': ''}}]}
dados['features'] = [feature for feature in dados['features'] if int(feature['properties']['id'][0:2]) in [41,42,43]]

# for feature in dados['features']:
#     id = feature['properties']['id']
#     if not int(id[0:2]) in [41,42,43]:
#         #print ("{} - {}".format(feature['properties']['id'], feature['properties']['name']))

# grava novamente
with open('geojs-sul-mun.json', 'w') as g:
    json.dump(dados, g)

print('feito')