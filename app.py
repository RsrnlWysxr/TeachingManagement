# -*- encoding: utf-8 -*-

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"nickname": "xxy", "age": 18, "sex": "1"})


@app.route('/login', methods=['GET'])
def login():
    return 'login'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
