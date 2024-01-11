from flask import Flask, request, jsonify
from update_vals import gerar_exchange_rate


app = Flask(__name__)

exchange_rates = {}

@app.route('/convert', methods=['GET'])
def convert_currency():
    global exchange_rates
    exchange_rates = gerar_exchange_rate(exchange_rates)
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    try:
        amount = float(request.args.get('amount'))
    except:
        amount = 1

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return jsonify({'error': 'Moeda não suportada'}), 400

    if amount <= 0:
        return jsonify({'error': 'O valor a ser convertido deve ser maior que zero'}), 400

    result = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]

    response = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'result': result
    }

    return jsonify(response)

@app.route('/currencies', methods=['GET'])
def get_supported_currencies():
    global exchange_rates
    exchange_rates = gerar_exchange_rate(exchange_rates)
    return jsonify({'currencies': list(exchange_rates.keys())})


@app.route('/add_currency', methods=['POST'])
def add_currency():
    global exchange_rates
    exchange_rates = gerar_exchange_rate(exchange_rates)
    data = request.get_json()
    

    currency_code = data.get('currency')
    try:
        exchange_rate = data.get('exchange_rate')
    except:
        exchange_rate = 1
    
    if not currency_code or not exchange_rate:
        return jsonify({'error': 'Informe a moeda e a cotação'}), 400
    
    if currency_code in exchange_rates.keys():
        return jsonify({'error': 'Moeda já cadastrada'}), 400

    exchange_rates[currency_code] = float(exchange_rate)

    return jsonify({'success': f'Moeda {currency_code} adicionada com sucesso'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


