import investpy


class InfoAtivos:
    def __init__(self) -> None:
        self.pais = 'Brazil'

    def pesquisa(self, ativo, pais = None):
        if pais is not None and not isinstance(pais, str):
            return "ERR#001: país especificado inválido"
            
        if ativo is None:
            return "ERR#002: Ativo não pode ser vazio"

        try:
            dados = investpy.search_quotes(text=ativo, countries=[self.pais])
        except ValueError:
            return "ERR#003: Ativo "+ ativo + " não encontrado"

        values = {}
        for dado in dados:
            values = dado.__dict__

        return values

infoAtivos = InfoAtivos()