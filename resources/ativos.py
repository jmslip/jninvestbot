from flask_restplus import Resource

from services.infoAtivos import infoAtivos
from services.rotinas import rotinas
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

@api.route('/atualiza-historico')
class Rotina(Resource):
    @staticmethod
    def post():
        response = api.payload
        ativos = response['ativos']
        return rotinas.atualiza_historico(ativos)