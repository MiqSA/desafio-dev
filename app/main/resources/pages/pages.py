from flask import Blueprint, render_template
import requests

pages_blueprint = Blueprint('pages', __name__, template_folder='app/main/templates')


@pages_blueprint.route('/')
def index():
    transactions = requests.get('http://0.0.0.0:5057/v1.0/stores/transactions')
    transactions = transactions.json()

    total = requests.get('http://0.0.0.0:5057/v1.0/stores/transactions/total')
    total = total.json()
    return render_template('home.html', transactions=transactions['results'], total=total['results'])


@pages_blueprint.route('/upload')
def upload():
    return render_template('uploads.html')



