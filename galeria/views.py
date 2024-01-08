from django.shortcuts import render

def index(request):
    dados = {
        1: {
            'nome': 'Nebulosa de Carina',
            'legenda': 'webbtelescope / NASA / James Webb'
        },
        2: {
            'nome': 'Galaxia NGC 1079',
            'legenda': 'webbtelescope / NASA / Hubble'
        }
    }
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')