# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify
from libs.dealJson import dealJson
from logic.login import onLogin
from logic.course import onCourse
from logic.signin import onSignin

route_api = Blueprint('api', __name__)


@route_api.route('/login', methods=['GET', 'POST'])
def login():
    data = dealJson()
    return jsonify(onLogin(data))


@route_api.route('/course', methods=['GET', 'POST'])
def course():
    return jsonify(onCourse())


@route_api.route('/signin', methods=['GET', 'POST'])
def Signin():
    data = dealJson()
    return jsonify(onSignin(data))
