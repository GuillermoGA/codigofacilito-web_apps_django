from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {
        'message': 'Listado de productos',
        'title': 'Prodi¡uctos',
        'products': [
            {'title': 'Playera', 'price': 5, 'stock': True},
            {'title': 'Camisa', 'price': 7, 'stock': True},
            {'title': 'Mochila', 'price': 20, 'stock': False},
        ]
    })
