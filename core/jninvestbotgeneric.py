class JnInvestBotGeneric:

    def gera_resposta(self, mensagem):
        response = {}
        status = 200
        if mensagem is None:
            status = 400
            mensagem = "ERR#04: Erro ao processar"
        elif isinstance(mensagem, str):
            if mensagem.startswith('ERR#01') or mensagem.startswith('ERR#02'):
                status = 400
            elif mensagem.startswith('ERR#03'):
                status = 204
        
        response['status'] = status
        response['resposta'] = mensagem
        
        return response

jninvestbot_generic = JnInvestBotGeneric()