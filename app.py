# -*- encoding: utf-8 -*-
"""
封装app变量以及db变量
"""

from flask import Flask
from dbMoudle.db import db
from initdb import initdb
from controllers.index import route_index
from controllers.api import route_api

""" class Application(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.config.from_pyfile('setting/basicsetting.py')

        db.init_app(self) """


def create_app():
    app = Flask(__name__)
    """
    from_object参数需要模块路径
    app.config是dict的子类
    要求所有字母大写,存在小写会忽略
    存在默认值
    """
    app.config.from_pyfile('setting/basicsetting.py')

    app.register_blueprint(route_index, url_prefix='/')
    app.register_blueprint(route_api, url_prefix='/api')

    db.init_app(app)
    with app.app_context():
        initdb(db, app)
    return app
