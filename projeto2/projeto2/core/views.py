from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from core.models import FeriadoModel



def ver_feriado(request):
    qs = FeriadoModel.objects.all()
    data_atual = date.today()
    feriado = 'Hoje não é feriado!'
    contexto = {
    'feriado': feriado
    }
            

    for feriado in qs:
        if(feriado.dia == data_atual.day and feriado.mes == data_atual.month):
            feriado = feriado.nome
            contexto = {
                'feriado': feriado
            } 
        break
    return render(request, 'feriado.html', contexto)

