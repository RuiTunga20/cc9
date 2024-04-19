from django.shortcuts import render
from landpage.models import *
import os
import zipfile
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path


def download_folder(request,id):
    # Caminho da pasta que contém os arquivos que deseja baixar
    BASE_DIR = Path(__file__).resolve().parent.parent


    folder_path = os.path.join(settings.MEDIA_ROOT, id)

    print(folder_path)
    #print(id)



    # Nome do arquivo zip que será criado
    zip_filename = id+'.zip'

    # Cria um arquivo zip
    zip_file = zipfile.ZipFile(zip_filename, 'w')

    # Adiciona todos os arquivos da pasta ao arquivo zip
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    # Fecha o arquivo zip
    zip_file.close()

    # Cria uma resposta de download para o arquivo zip
    response = HttpResponse(open(zip_filename, 'rb').read())
    response['Content-Type'] = 'application/zip'
    response['Content-Disposition'] = 'attachment; filename="%s"' % zip_filename

    # Retorna a resposta de download
    return response


def home(request):
    Prelectores= prelector.objects.all()
    Moderador= moderador.objects.all()
    Dia_1=Programa1.objects.all()
    Dia_2=Programa2.objects.all()
    Noticias=NOTICIA.objects.all()

    context={
        'Prelectores':Prelectores,
        'Moderador':Moderador,
        'Dia_1':Dia_1,
        'Dia_2':Dia_2,
        'Noticias':Noticias,

    }


    return render(request,'index.html',context)