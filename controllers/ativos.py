from flask_restplus import Resource
from services.infoAtivos import infoAtivos
from core.hrbrokerGeneric import hrbrokerGeneric

from core.server import server

app = server.app
api = server.api


@api.route('/ativos')
class Ativos(Resource):
    @staticmethod
    def post():
        response = api.payload
        nome = response["nome"]

        return hrbrokerGeneric.gera_resposta(mensagem=infoAtivos.pesquisa(nome)) 
