from flask import request, render_template, session, redirect, url_for
from app import app
from scipy.optimize import linprog

from app.utils.form_utils import *
from app.utils.post_optimization_utils import restrictions_right_change_dict_to_list


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('form.html', num_variables=0, num_restrictions=0)


@app.route('/initiate_simplex', methods=['POST'])
def initiate_simplex():
    num_variables = None
    num_restrictions = None
    labels = []
    operators = []
    if request.method == 'POST':
        num_variables = int(request.form['num_variables'])
        num_restrictions = int(request.form['num_restrictions'])
        labels = [chr(65 + i) for i in range(num_variables)]
        operators = ['<=', '>=']

    session['labels'] = labels

    return render_template('form.html', num_variables=num_variables, num_restrictions=num_restrictions,
                           labels=labels, operators=operators)


@app.route('/process', methods=['POST'])
def process():
    restrictions_right_list = restrictions_right_dict_to_list({
        key: int(value) for key, value in request.form.items() if key.startswith('value_right')
    })
    restrictions_operators = {
        key: value for key, value in request.form.items() if key.startswith('operator')
    }
    variables = {
        key: -int(value)
        for key, value in request.form.items()
        if key.startswith('variable')
    }
    variables_list = variables_dict_to_list(variables)

    num_variables = len(variables)
    labels = session.get('labels')
    num_restrictions = len(restrictions_right_list)
    restrictions_list = restrictions_dict_to_list({
        key: int(value) for key, value in request.form.items() if key.startswith('restriction')
    }, num_restrictions)
    restrictions_list, restrictions_right_list = invert_restriction_signs(restrictions_operators, restrictions_list,
                                                                          restrictions_right_list)

    session["restrictions_right_list"] = restrictions_right_list
    session["restrictions_operators"] = restrictions_operators
    session["variables_list"] = variables_list
    session["labels"] = labels
    session["restrictions_list"] = restrictions_list

    result = linprog(variables_list, restrictions_list, restrictions_right_list, method="highs")

    return render_template('result.html', objective_fuction=-result.fun, variables_results=result.x,
                           shadow_price=result.slack, labels=labels, num_variables=num_variables,
                           num_restrictions=num_restrictions, )


@app.route('/sensitivity_analysis', methods=['GET', 'POST'])
def sensitivity_analysis():
    restriction_right_change_list = restrictions_right_change_dict_to_list(
        {key: int(value) for key, value in request.form.items() if key.startswith('restriction_right_change')})

    variables_list = session.get('variables_list')
    restrictions_list = session.get('restrictions_list')
    restrictions_right_list = session.get('restrictions_right_list')
    new_restrictions_right_list = soma = [a + b for a, b in zip(restrictions_right_list, restriction_right_change_list)]

    new_result = linprog(variables_list, restrictions_list, new_restrictions_right_list, method="highs")

    return render_template('post_optimization.html',
                           objective_fuction=-new_result.fun,
                           variables_results=new_result.x,
                           shadow_price=new_result.slack,
                           result=new_result.status,
                           num_variables=len(variables_list),
                           num_restrictions=len(restrictions_right_list),
                           labels=session.get('labels'))


@app.route('/reset', methods=['GET'])
def reset():
    session.clear()
    return redirect(url_for('home'))
