from flask import Flask
from here import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/here')

if __name__ == '__main__':
    app.run(debug=True)
