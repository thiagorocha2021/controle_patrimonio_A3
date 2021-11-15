
import requests
import json

from requests import head


class IBGE():
    
    var1 = 5

    def estadoBrasil():
        var2 = 5
        
        endPoint = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome'
        data = requests.request(method='GET',url=endPoint)
        estados = data.json() 
        listaEstado = []
    
        for a in estados:
            listaEstado.append(a['nome'])

        #return None
        return listaEstado    
    

    def pais():
        endPoint = 'https://servicodados.ibge.gov.br/api/v1/localidades/paises?orderBy=nome'
        data = requests.request(method='GET',url=endPoint)
        pais = data.json() 
        listaPais = []
    
        for a in pais:
            listaPais.append(a['nome'])
        #estados = sorted(listaEstado)
        return listaPais    


class MercadoLivre():

    def cotegorias():

        endPont = 'https://api.mercadolibre.com/sites/MLB/categories'
        token = ''

        listaCategoria = []
        headers = {'Authorization':'Bearer {}'.format(token),
                    'Content-Type':'application/json'}
        data = requests.request(method='GET', url=endPont, headers=headers)

        for a in data.json():
            listaCategoria.append(a['name'])
        listaCategoria = sorted(listaCategoria)
        
        #return None
        return listaCategoria



def API_IBGE_is_on():
    
    url = 'https://api.mercadolibre.com/sites/MLB/categories'

    try:
        response = head(url)
    except ConnectionError:
        return False

    return 200 <= response.status_code <= 400

def API_ML_is_on():
    
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/paises?orderBy=nome'

    try:
        response = head(url)
    except ConnectionError:
        return False

    return 200 <= response.status_code <= 400