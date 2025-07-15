
from flask import Flask, render_template, request
from nbp_fetcher import fetch_exchange_rates

app = Flask(__name__)

# Przy starcie od razu pobieramy dane
rates = fetch_exchange_rates()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_code = None
    amount = None

    if request.method == 'POST':
        selected_code = request.form['currency']
        amount = float(request.form['amount'])
        rate = next((r for r in rates if r['code'] == selected_code), None)

        if rate:
            result = round(amount * rate['ask'], 2)

    return render_template('index.html', rates=rates, result=result, code=selected_code, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)