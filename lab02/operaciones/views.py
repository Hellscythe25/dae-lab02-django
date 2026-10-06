import math

from django.shortcuts import redirect, render

from lab02.utilidades import a_numero, formatear

# clave del formulario -> (nombre en el mensaje, símbolo)
OPERACIONES = {
    'suma': ('suma', '+'),
    'resta': ('resta', '-'),
    'multiplicacion': ('multiplicación', '×'),
}


def index(request):
    context = {
        'titulo': 'Operaciones',
        'operaciones': OPERACIONES,
    }
    return render(request, 'operaciones/formulario.html', context)


def resultado(request):
    if request.method != 'POST':
        return redirect('operaciones:index')

    primero = a_numero(request.POST.get('numero1'))
    segundo = a_numero(request.POST.get('numero2'))
    clave = request.POST.get('operacion')

    error = None
    if primero is None or segundo is None or clave not in OPERACIONES:
        error = 'Ingresa dos números válidos y elige una operación.'
    else:
        if clave == 'suma':
            valor = primero + segundo
        elif clave == 'resta':
            valor = primero - segundo
        else:
            valor = primero * segundo
        if not math.isfinite(valor):
            error = 'El resultado es demasiado grande para mostrarlo.'

    if error:
        context = {
            'titulo': 'Operaciones',
            'operaciones': OPERACIONES,
            'error': error,
        }
        return render(request, 'operaciones/formulario.html', context)

    nombre, simbolo = OPERACIONES[clave]
    context = {
        'titulo': 'Resultado',
        'mensaje': 'La {} de {} {} {} = {}'.format(
            nombre, formatear(primero), simbolo, formatear(segundo), formatear(valor)
        ),
    }
    return render(request, 'operaciones/resultado.html', context)
