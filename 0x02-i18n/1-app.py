#!/usr/bin/env python3
"""handling request to root URL /"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """index page"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)













# #!/usr/bin/env python3
# """handling request to root URL /"""
# from flask import Flask, render_template
# from flask_babel import Babel


# app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
# babel = Babel(app)