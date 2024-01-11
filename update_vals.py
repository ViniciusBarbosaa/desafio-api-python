import requests
import logging


logger = logging.getLogger(__name__)

def obter_cotacoes_da_api(exchange_rates, api_url='https://economia.awesomeapi.com.br/json/last/'):
    try:
        codes = _obter_modedas(exchange_rates)
        url_da_api = f"{api_url}{codes}"

        response = requests.get(url_da_api)
        response.raise_for_status()  # Levanta uma exceção em caso de código de status de erro

        dados_cotacoes = response.json()

        rate = {}
        for value in dados_cotacoes.values():
            rate[value.get('codein')] = value.get('low')

        return rate
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise

def _obter_modedas(exchange_rates):
    url_code = ''
    
    for key, _ in exchange_rates.items():
        if key not in ['BTC', 'ETH', 'USD']:
            url_code += f'USD-{key},'
    
    
    return url_code[:-1]


def gerar_exchange_rate(exchange_rates):
    vals = obter_cotacoes_da_api(exchange_rates)
    
    if exchange_rates is None or not exchange_rates:
        exchange_rates = {
            'USD': 1.0,
            'BRL': 5.5,
            'EUR': 0.9,
            'BTC': 0.0002,
            'ETH': 0.005
        }
    
    if vals:
        for key, value in vals.items():
            if key in exchange_rates:
                exchange_rates[key] = float(value)
    
    return exchange_rates
    

    
