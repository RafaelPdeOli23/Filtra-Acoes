class Acoes:
    def __init__(self, papel, cotacao, p_l, p_vp, div_yield, roic, roe):
        self.papel = papel
        self.cotacao = cotacao
        self.p_l = p_l
        self.p_vp = p_vp
        self.div_yield = div_yield
        self.roic = roic
        self.roe = roe

class Estrategia:
    def __init__(self, p_l_maximo=1000, p_vp_maximo=1000, div_yield_minimo=0, roic_minimo=0, roe_minimo=0):
        self.p_lmaximo = p_l_maximo
        self.p_vp_maximo = p_vp_maximo
        self.div_yield_minimo = div_yield_minimo
        self.roic_minimo = roic_minimo
        self.roe_minimo = roe_minimo

    def aplicar_estrategia(self, acao: Acoes):
        if acao.p_l > self.p_lmaximo \
                or acao.p_vp > self.p_vp_maximo \
                or acao.div_yield < self.div_yield_minimo \
                or acao.roic < self.roic_minimo \
                or acao.roe < self.roe_minimo:
            return False

        else:
            return True
