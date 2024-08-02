from ..models import Theme, Rent
from datetime import datetime


class Util:

    def calculaDesconto(self, theme_id, cliente, date):

        theme = Theme.objects.get(pk=theme_id)

        isRent = Rent.objects.filter(client=cliente).exists()

        try:
            data = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("A data do tema não está no formato correto.")
        
        dia_semana = data.weekday()
        valor = theme.price

        if(isRent):
            valor -= valor *0.10
        if(dia_semana >= 0 and dia_semana < 4 ):
            valor -= valor *0.40
        
        return valor