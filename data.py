import requests
import json
import locale
    
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')  

def buscar_dados():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    return json.loads(request.content)

def buscar_cotacao():
    dados= buscar_dados() 
    return locale.currency(float(dados['USDBRL']['high']))

def calcular_cotacao(value):
    dados= buscar_dados()
    calculo= float(value)/float(dados['USDBRL']['high'])
    
    return locale.currency(calculo, grouping=True, symbol=None)
    