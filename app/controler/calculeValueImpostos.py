from app.controler.teste import valorFretes


def valor_frete(valor,frete):
    return valor+frete


def valor_icms(valor,ICMS):
    valorICMS = (ICMS*valor/100)
    return valorICMS

def valor_ipi(valor,IPI):
    
    valorIPI = (IPI*valor/100)
    return valorIPI