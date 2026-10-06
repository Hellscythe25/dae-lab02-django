import math
from decimal import Decimal


def a_numero(texto):
    """Convierte un texto a float aceptando coma o punto decimal.

    Devuelve None si el texto está vacío o no es un número finito.
    """
    if texto is None:
        return None
    try:
        numero = float(texto.strip().replace(',', '.'))
    except ValueError:
        return None
    if not math.isfinite(numero):
        return None
    return numero


def formatear(numero, decimales=10):
    """Muestra un número sin notación científica ni ceros sobrantes.

    37.0 se muestra como 37 y 0.1 + 0.2 como 0.3.
    """
    redondeado = round(numero, decimales) + 0.0  # + 0.0 evita "-0"
    texto = format(Decimal(str(redondeado)), 'f')
    if '.' in texto:
        texto = texto.rstrip('0').rstrip('.')
    return texto
