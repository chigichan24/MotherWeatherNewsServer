from flask import Flask, render_template
from flask_cors import CORS
from api import api, sensors, weather
import os

app = Flask(__name__, static_url_path='')
CORS(app)
cf_port = int(os.getenv("PORT", 8080))

app.register_blueprint(api.app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=cf_port)
