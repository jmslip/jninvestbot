import investpy
import json


class InfoAtivos:
    def __init__(self) -> None:
        self.pais = 'Brazil'

    def pesquisa(self, ativo, pais = None, to_dict=True):
        if pais is not None and not isinstance(pais, str):
            return "ERR#001: país especificado inválido"
            
        if ativo is None:
            return "ERR#002: Ativo não pode ser vazio"

        try:
            dados = investpy.search_quotes(text=ativo, countries=[self.pais])
        except ValueError:
            return "ERR#003: Ativo "+ ativo + " não encontrado"

        for dado in dados[:1]:
            if to_dict:
                return dado.__dict__

        return dados

    def historico(self, ativo, de_data=None, ate_data=None, historico_recente=False, to_dict=False, to_json=True):
        pesquisa = self.pesquisa(ativo, to_dict=to_dict)

        historico = 0
        for hist in pesquisa:
            if historico_recente:
                historico = hist.retrieve_recent_data().tail(2)
            else:
                historico = hist.retrieve_historical_data(from_date=de_data, to_date=ate_data)
        
        if to_json:
            return json.loads(historico.to_json(orient='index', date_format='iso', compression='gzip'))

        return historico

infoAtivos = InfoAtivos()