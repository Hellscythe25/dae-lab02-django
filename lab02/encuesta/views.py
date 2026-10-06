from django.shortcuts import redirect, render


def index(request):
    context = {
        'titulo': 'Formulario',
    }
    return render(request, 'encuesta/formulario.html', context)


def enviar(request):
    if request.method != 'POST':
        return redirect('encuesta:index')
    context = {
        'titulo': 'Respuesta',
        'nombre': request.POST.get('nombre', ''),
        # La contraseña no se muestra: solo se indica que fue recibida.
        'clave': '*' * len(request.POST.get('password', '')),
        'educacion': request.POST.get('educacion', ''),
        'nacionalidad': request.POST.get('nacionalidad', 'No indicada'),
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST.get('email', ''),
        'website': request.POST.get('sitioweb', ''),
    }
    return render(request, 'encuesta/respuesta.html', context)
