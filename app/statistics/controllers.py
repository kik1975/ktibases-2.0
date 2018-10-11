from flask import Blueprint,render_template

module = Blueprint('statistics', __name__,url_prefix='/statistics')

@module.route('/', methods=['GET'])
def index():
    return render_template('statistics/statistics.html')
