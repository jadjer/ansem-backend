import os

from flask import Flask

from ansem.auth import auth
# from srs.person.list import person_list
# from srs.person.detail import person_detail
from ansem.db import init_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=b'e02d3a100e849c3cf396',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth)
    # app.register_blueprint(person_list)
    # app.register_blueprint(person_detail)

    db.init_app(app)

    return app
