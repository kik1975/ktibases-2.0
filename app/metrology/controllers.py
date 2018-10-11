from flask import Blueprint,render_template

module = Blueprint('metrology', __name__,url_prefix='/metrology')

@module.route('/', methods=['GET'])
def index():
    return render_template('metrology/metrology.html')
