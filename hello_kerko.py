import pathlib

from flask import Flask
from kerko.composer import Composer

def cusacklab():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kD%CwAWo#D&F5n07'  # Replace this value.
    app.config['KERKO_ZOTERO_API_KEY'] = '2jTxk56Cboj4CI0a1x6HI62y'  # Replace this value.
    app.config['KERKO_ZOTERO_LIBRARY_ID'] = '180445'  # Replace this value.
    app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = 'group'  # Replace this value if necessary.
    app.config['KERKO_DATA_DIR'] = str(pathlib.Path(__file__).parent / 'data' / 'kerko')
    app.config['KERKO_COMPOSER'] = Composer()

    from flask_babelex import Babel
    from flask_bootstrap import Bootstrap

    babel = Babel(app)
    bootstrap = Bootstrap(app)

    from kerko import blueprint as kerko_blueprint

    app.register_blueprint(kerko_blueprint, url_prefix='/bibliography')