from services.infoAtivos import infoAtivos


class Rotinas:

    def __init__(self) -> None:
        self.str_yesterday = 'yesterday'
        self.str_today = 'today'
        self.str_var = 'var'
        self.str_close = 'Close'
        self.str_simbolo = 'simbolo'

    def atualiza_historico(self, ativos):
        historicos = dict()
        for ativo in ativos:
            info_ativos = infoAtivos.historico(ativo=ativo[self.str_simbolo], historico_recente=True, to_json=True)
            var = dict()
            yesterday_key = today_key = ''
            for key, value in info_ativos.items():
                if self.str_yesterday in var:
                    today_key = key
                    var[self.str_today] = value[self.str_close]
                else:
                    yesterday_key = key
                    var[self.str_yesterday] = value[self.str_close]

            info_ativos[today_key][self.str_var] = self.get_calculo_var(var[self.str_today], var[self.str_yesterday])
            info_ativos.pop(yesterday_key)
            
            historicos[ativo[self.str_simbolo]] = info_ativos
        return historicos

    def get_calculo_var(self, last_price_today, last_price_yesterday):
        return round(((last_price_yesterday - last_price_today) / last_price_yesterday), 4) * -1

rotinas = Rotinas()
