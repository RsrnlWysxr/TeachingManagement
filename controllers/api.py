# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify
from libs.dealJson import dealJson
from logic.login import onLogin

route_api = Blueprint('api', __name__)


@route_api.route('/login', methods=['GET', 'POST'])
def login():
    data = dealJson()
    return jsonify(onLogin(data))
