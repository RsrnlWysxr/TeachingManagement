# -*- encoding: utf-8 -*-

from flask import request, json


def dealJson():
    return json.loads(request.get_data().decode('utf-8'))
