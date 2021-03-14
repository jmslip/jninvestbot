import pandas
from services.infoAtivos import infoAtivos

class Calculos:

    def __init__(self):
        self.close = 'Close'
        self.simbolo = 'simbolo'

    def covariancia(self, ativos):
        historico = 0
        historicos = dict()
        indice_dict = 0
        for ativo in ativos:
            historico = infoAtivos.historico(ativo['simbolo'], de_data='31/01/2020' ,ate_data='03/02/2021')
            
            df = pandas.DataFrame({
                ativo[self.simbolo]: self.get_calculo_var(historico[self.close].values[1], historico[self.close].values[0])
            }, index=[0])

            for hist in range(historico[self.close].count()):
                i = hist + 2
                df.loc[i-1] = [self.get_calculo_var(historico[self.close].values[hist], historico[self.close].values[hist-1])]
                if hist >= (historico[self.close].count()):
                    break
            historicos[indice_dict] = df
            indice_dict = indice_dict + 1
        
        # df = 0
        # df = pandas.DataFrame.from_dict(historicos, orient='index')

        # for cov in range(historicos[0]['Close'].count()):
        #     df.loc[i-1] = [self.get_calculo_var(historico[self.close].values[i], historico[self.close].values[i-1]), self.get_calculo_var(his)]
        cov = pandas.concat(historicos)
        print(cov)

    def get_calculo_var(self, last_price_today, last_price_yesterday):
        return round(((last_price_yesterday - last_price_today) / last_price_yesterday), 4) * -1


calculos = Calculos()