from flask import render_template,Blueprint,make_response
from app import app
mod = Blueprint('transaction', __name__, url_prefix='/api/v1')


'''handelling route errors'''

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response


@app.route('/')
@app.route('/index')
def index():
    first_variable = "Hello World"
    title = "Welcome to Flask"
    return render_template('index.html', title='Home', first_variable=first_variable)
