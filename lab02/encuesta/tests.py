from django.test import TestCase
from django.urls import reverse


class EncuestaTests(TestCase):
    def test_formulario_se_muestra(self):
        r = self.client.get(reverse('encuesta:index'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'csrfmiddlewaretoken')
        self.assertContains(r, 'action="/encuesta/enviar"')

    def test_respuesta_muestra_datos(self):
        r = self.client.post(reverse('encuesta:enviar'), {
            'nombre': 'Ana', 'password': 'secreta', 'educacion': 'universidad',
            'nacionalidad': 'hispana', 'idiomas': ['español', 'inglés'],
            'email': 'ana@mail.com', 'sitioweb': 'ana.com',
        })
        self.assertContains(r, 'Ana')
        self.assertContains(r, 'universidad')
        self.assertContains(r, 'hispana')
        self.assertContains(r, 'inglés')
        self.assertContains(r, 'ana@mail.com')
        self.assertNotContains(r, 'secreta')

    def test_nacionalidad_vacia_no_falla(self):
        r = self.client.post(reverse('encuesta:enviar'), {'nombre': 'Ana'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'No indicada')

    def test_get_en_enviar_redirige(self):
        r = self.client.get(reverse('encuesta:enviar'))
        self.assertRedirects(r, reverse('encuesta:index'))
