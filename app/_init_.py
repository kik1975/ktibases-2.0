import os
from flask import Flask

from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.auth.controllers as auth
    import app.metrology.controllers as metrology
    import app.statistics.controllers as statistics

    app.register_blueprint(statistics.module)
    app.register_blueprint(auth.module)
    app.register_blueprint(metrology.module)

    return app
