from flask_restplus import Resource
from services.infoAtivos import infoAtivos
from core.jninvestbotgeneric import jninvestbot_generic

from core.server import server

app = server.app
api = server.api


@api.route('/ativos')
class Ativos(Resource):
    @staticmethod
    def get():
        response = api.payload
        nome = response["nome"]

        return jninvestbot_generic.gera_resposta(mensagem=infoAtivos.pesquisa(nome))