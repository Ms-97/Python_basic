from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify


app = Flask(__name__,static_url_path='')

@app.route('/')
@app.route('/omok')

def omok():
    return render_template('omok3_19.html')


if __name__ == '__main__':
    app.run(debug=True)
    