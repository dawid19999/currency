
from flask import Flask, render_template, request
from nbp_fetcher import fetch_exchange_rates

app = Flask(__name__)


rates_list = fetch_exchange_rates()
rates_dict = {rate['code']: rate for rate in rates_list}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_code = None
    amount = None

    if request.method == 'POST':
        selected_code = request.form['currency']
        amount = float(request.form['amount'])

        rate = rates_dict.get(selected_code)
        

        if rate:
            result = round(amount * rate['ask'], 2)

    return render_template('index.html', rates=rates_list, result=result, code=selected_code, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
