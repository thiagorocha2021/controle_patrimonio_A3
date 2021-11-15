import app.controler.APIexternas as API
from app.model.models import (
    Filial,
    Colaborador,
    Fornecedor,
    Patrimonio,
)



class Total():
    def total():

        coladorador = Colaborador.query.count()
        patrimonio = Patrimonio.query.count()
        fornecedor = Fornecedor.query.count()
        filial = Filial.query.count()
        
        data = {'coladorador': coladorador,
                'patrimonio': patrimonio,
                'fornecedor': fornecedor,
                'filial': filial}
        
        
        return data