from flask_restplus import Api
from flask import Blueprint

from app.main.controller.campaign_controller import api as reg_ns


blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Email Backend',
    version='1.0',
    description='rest api in flask',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(reg_ns, path='/')
