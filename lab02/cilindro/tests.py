from django.test import TestCase
from django.urls import reverse


class CilindroTests(TestCase):
    def calcular(self, diametro, altura):
        return self.client.post(reverse('cilindro:calcular'),
                                {'diametro': diametro, 'altura': altura})

    def test_volumen_del_ejemplo(self):
        r = self.calcular('2,15', '1,75')
        self.assertContains(r, 'El volumen del cilindro es de 6.35338026803 metros cúbicos')

    def test_acepta_punto_decimal(self):
        self.assertContains(self.calcular('2.15', '1.75'), '6.35338026803')

    def test_medidas_enormes_no_dan_500(self):
        for d in ['1e155', '1e200', '1e308']:
            r = self.calcular(d, '1')
            self.assertEqual(r.status_code, 200)
            self.assertContains(r, 'demasiado grandes')

    def test_sin_notacion_cientifica(self):
        self.assertContains(self.calcular('1e-3', '1'), 'es de 0.0000007854 metros')
        self.assertNotContains(self.calcular('1e8', '1'), 'e+')

    def test_valores_invalidos(self):
        for d, h in [('', '1'), ('x', '1'), ('0', '1'), ('-2', '1'), ('1', '0')]:
            r = self.calcular(d, h)
            self.assertContains(r, 'mayores que cero')
