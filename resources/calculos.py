from flask_restplus import Resource

from services.calculos import calculos

from core.server import server

app = server.app
api = server.api


@api.route('/calculos/ray-dalio')
class RayDalio(Resource):
    def get(self):
        response = api.payload
        ativos = response['ativos']

        calculos.covariancia(ativos=ativos)

        return ativos