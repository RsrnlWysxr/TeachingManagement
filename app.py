# -*- encoding: utf-8 -*-
"""
封装app变量以及db变量
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.config.from_pyfile('setting/basicsetting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
