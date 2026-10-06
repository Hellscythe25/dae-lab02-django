from django.test import TestCase
from django.urls import reverse


class OperacionesTests(TestCase):
    def operar(self, n1, n2, op):
        return self.client.post(reverse('operaciones:resultado'),
                                {'numero1': n1, 'numero2': n2, 'operacion': op})

    def test_suma(self):
        self.assertContains(self.operar('18', '19', 'suma'), 'La suma de 18 + 19 = 37')

    def test_resta(self):
        self.assertContains(self.operar('18', '19', 'resta'), 'La resta de 18 - 19 = -1')

    def test_multiplicacion(self):
        self.assertContains(self.operar('18', '19', 'multiplicacion'),
                            'La multiplicación de 18 × 19 = 342')

    def test_decimales_con_coma(self):
        self.assertContains(self.operar('1,5', '2', 'suma'), 'La suma de 1.5 + 2 = 3.5')

    def test_resultado_desbordado_no_da_500(self):
        for op in ['suma', 'multiplicacion']:
            r = self.operar('1e308', '1e308' if op == 'suma' else '10', op)
            self.assertEqual(r.status_code, 200)
            self.assertContains(r, 'demasiado grande')

    def test_formato_sin_ruido_de_coma_flotante(self):
        self.assertContains(self.operar('0.1', '0.2', 'suma'), 'La suma de 0.1 + 0.2 = 0.3')
        self.assertContains(self.operar('1e-7', '0', 'suma'), '0.0000001 + 0 = 0.0000001')

    def test_entrada_invalida_muestra_error(self):
        r = self.operar('abc', '2', 'suma')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Ingresa dos números válidos')

    def test_operacion_desconocida(self):
        self.assertContains(self.operar('1', '2', 'division'), 'Ingresa dos números válidos')
