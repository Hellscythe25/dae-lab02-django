# Actividad 1: Revisión de conceptos

| Concepto / Principio | Definición, comentarios o interpretación |
|---|---|
| 1. Controlador (View) en Django | Es una función de Python que recibe la petición del navegador (`request`) y decide qué responder. En Django hace el papel de controlador: lee los datos que llegan, hace los cálculos necesarios y devuelve una respuesta, normalmente una página HTML. En el laboratorio, `index` solo muestra el formulario y `enviar` procesa lo que el usuario escribió. |
| 2. Paso de datos a plantillas (context) | El `context` es un diccionario que la vista envía a la plantilla. Cada clave se convierte en una variable que la plantilla puede mostrar con `{{ variable }}`. Así la lógica queda en la vista y el HTML solo se encarga de mostrar. Por ejemplo, `{'titulo': 'Formulario'}` hace que `{{ titulo }}` muestre "Formulario". |
| 3. Flujo Request-Response | El navegador envía una petición a una URL. Django la compara con las rutas de `urls.py`, ejecuta la vista asociada y esta devuelve una respuesta que el navegador muestra. En el laboratorio, enviar el formulario genera una petición POST a `/encuesta/enviar`, la vista lee `request.POST` y responde con la página de resultados. |
| 4. Renderización de templates | Es el proceso de combinar una plantilla HTML con los datos del `context` para producir el HTML final. La función `render(request, 'plantilla.html', context)` reemplaza las variables y ejecuta las etiquetas como `{% for %}` o `{% url %}`. El navegador solo recibe el resultado ya armado. |
