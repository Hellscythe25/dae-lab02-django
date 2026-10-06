import math

from django.shortcuts import redirect, render

from lab02.utilidades import a_numero, formatear

TITULO = 'Cálculo del volumen de un cilindro'


def index(request):
    context = {
        'titulo': TITULO,
    }
    return render(request, 'cilindro/formulario.html', context)


def calcular(request):
    if request.method != 'POST':
        return redirect('cilindro:index')

    diametro = a_numero(request.POST.get('diametro'))
    altura = a_numero(request.POST.get('altura'))

    error = None
    if diametro is None or altura is None or diametro <= 0 or altura <= 0:
        error = 'Ingresa un diámetro y una altura mayores que cero.'
    else:
        radio = diametro / 2
        try:
            volumen = math.pi * radio ** 2 * altura
        except OverflowError:
            volumen = math.inf
        if not math.isfinite(volumen):
            error = 'Las medidas son demasiado grandes para calcular el volumen.'

    if error:
        context = {
            'titulo': TITULO,
            'error': error,
        }
        return render(request, 'cilindro/formulario.html', context)

    context = {
        'titulo': 'Resultado',
        'volumen': formatear(volumen, 11),
    }
    return render(request, 'cilindro/resultado.html', context)
