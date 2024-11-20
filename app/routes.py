from flask import request, render_template
from app import app


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('form.html', num_variables=0, num_restrictions=0)


@app.route('/variables', methods=['POST', 'GET'])
def variables():
    num_variables = None
    num_restrictions = None
    if request.method == 'POST':
        num_variables = int(request.form['num_variables'])
        num_restrictions = int(request.form['num_restrictions'])
        labels = [chr(65 + i) for i in range(num_variables)]
        operators = ['<=', '>=']

    return render_template('form.html', num_variables=num_variables, num_restrictions=num_restrictions, labels=labels, operators=operators)


@app.route('/process', methods=['POST'])
def process():
    variables_data = {key: value for key, value in request.form.items()}
    return f"Valores recebidos: {variables_data}"
