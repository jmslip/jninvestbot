import investpy


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

        if to_dict:
            values = {}
            for dado in dados:
                values = dado.__dict__

            return values
        return dados

    def historico(self, ativo, de_data, ate_data):
        pesquisa = self.pesquisa(ativo, to_dict=False)

        historico = 0
        for hist in pesquisa:
            historico = hist.retrieve_historical_data(from_date=de_data, to_date=ate_data)
        
        return historico

infoAtivos = InfoAtivos()