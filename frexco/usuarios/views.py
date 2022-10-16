from datetime import datetime
from uuid import uuid4

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer


@csrf_exempt
def usuarios_salva(request):
    if request.method == 'POST':
        dados = JSONParser().parse(request)
        if not 'senha' in dados.keys():
            dados.update({'senha': str(uuid4())})

        dados['data_nascimento'] = datetime.date(
            datetime.strptime(dados['data_nascimento'], '%d/%m/%Y')
        )

        serializer = UsuarioSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(status=404)


@csrf_exempt
def usuarios_lista(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    return JsonResponse(serializer.errors, status=400)
