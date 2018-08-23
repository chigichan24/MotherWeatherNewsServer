from flask import Flask
import os

app = Flask(__name__, static_url_path='')
cf_port = int(os.getenv("PORT", 8000))

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=cf_port)
