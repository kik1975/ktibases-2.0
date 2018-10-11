from flask import Blueprint,render_template

module = Blueprint('auth', __name__)

@module.route('/', methods=['GET'])
def index():
    return render_template('auth/index.html')
