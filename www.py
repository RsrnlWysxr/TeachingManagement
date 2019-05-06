# -*- encoding: utf-8 -*-
from app import app
from controllers.index import route_index
from controllers.api import route_api


app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_api, url_prefix='/api')
