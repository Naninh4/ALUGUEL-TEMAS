from ..models import *
from datetime import datetime


class Util:

    def __init__(self):
        pass

    def calculaDesconto(self, theme_id, cliente):

        theme =  Theme.objects.get(Theme, pk=theme_id)

        isRent = Rent.objects.get(Rent, cliente = cliente)

        data = datetime.strptime(theme.price, 'Y%-%m-%d')
        dia_semana = data.weekday()

        if(isRent):
            valor -= valor *0.10
        if(dia_semana >= 0 and dia_semana < 4 ):
            valor -= valor *0.40
        
        return valor