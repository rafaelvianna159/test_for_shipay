from django.http import HttpResponse, JsonResponse
from .models import Estabelecimento,Recebimentos
from django.db.models import Sum
from .validator import validar_cnpj,validar_cpf
import json



def transacao(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if validar_cnpj(data['estabelecimento']) and validar_cpf(data['cliente']):

            estabelecimento = Estabelecimento.objects.get(cnpj = data['estabelecimento'])
            Recebimentos.objects.create(cliente=data['cliente'],valor=data['valor'],descricao=data['descricao'],Estabelecimento=estabelecimento)
            return JsonResponse({'aceito': True})
        return JsonResponse({'aceito':False})

    if request.method == "GET":
        cnpj=request.GET.get('cnpj')
        recebimentos = list( Recebimentos.objects.filter(Estabelecimento__cnpj=cnpj).values('cliente','valor','descricao'))
        estabelecimento = list(Estabelecimento.objects.filter(cnpj=cnpj).values('nome','cnpj','dono','telefone'))[0]
        total_recebido = Recebimentos.objects.aggregate(Sum('valor'))
        return JsonResponse({'estabelecimento':estabelecimento,'recebimentos': recebimentos, 'total_recebido':total_recebido['valor__sum']},safe=False)
    return JsonResponse({'erro':'methodo não aceito'})