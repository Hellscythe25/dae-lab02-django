# CLAUDE.md

Este archivo da contexto a Claude Code sobre este proyecto.

## Proyecto

- **Nombre:** DAE Laboratorios Remoto – Semana 2 (Tecsup, Desarrollo de Aplicaciones Web)
- **Tema:** Flujo de trabajo en Django: definir controladores (views) y pasar datos a las plantillas.
- **Enunciado:** `DAE_Laboratorio 2.docx` (en la raíz). El laboratorio es individual.
- **Estado:** código de las tres apps implementado y con pruebas (`python manage.py test`). Falta que el alumno grabe el video, tome las capturas finales y revise `docs/conclusiones.md` (borrador).

## Entorno

- Windows 11, PowerShell (Git Bash disponible).
- Python + Django, con entorno virtual `myvenv/` en la raíz del repo (ignorado por git).
- Servidor de desarrollo: `http://localhost:8000` (el docx dice 8080 por error).

## Estructura prevista

```
Semana 2/
├── CLAUDE.md
├── DAE_Laboratorio 2.docx
├── .claude/agents/        agentes del proyecto
├── myvenv/                entorno virtual (no se versiona)
├── lab02/                 proyecto Django (manage.py, lab02/settings.py, ...)
│   ├── encuesta/          Actividad 2: formulario + respuesta
│   ├── operaciones/       Tarea 1: dos números + operación (suma, resta, multiplicación)
│   └── cilindro/          Tarea 2: volumen del cilindro
└── docs/                  respuestas de la Actividad 1 y conclusiones
```

## Comandos

```powershell
myvenv\Scripts\activate
cd lab02
python manage.py runserver      # http://localhost:8000
python manage.py check
python manage.py test
```

Entorno nuevo desde cero: `python -m venv myvenv`, activar, `pip install django`.
El servidor también se puede lanzar desde `.claude/launch.json` (configuración `lab02`).

## Alcance del laboratorio

1. **Actividad 1:** tabla de conceptos (view, context, request-response, render) con palabras propias.
2. **Actividad 2:** app `encuesta` siguiendo el docx (formulario POST, vista `enviar`, `respuesta.html`, `{% csrf_token %}`).
3. **Tarea:** apps `operaciones` y `cilindro` en el mismo proyecto.
   - Operaciones: resultado tipo `La suma de 18 + 19 = 37`.
   - Cilindro: V = π·(d/2)²·h con diámetro y altura en metros. Ejemplo: d=2,15 y h=1,75 da 6.35338026803 m³ con `math.pi` (el docx muestra 6.35338096859 porque usa π≈3.141593).
4. **Entregables:** capturas de código y ejecución, video de máximo 4 minutos (lo graba el alumno) y conclusiones.

La rúbrica evalúa: views, paso de datos a la plantilla, URLs/enrutamiento, visualización en el template y la tarea adicional. También puntúan la puntualidad y la ortografía de las conclusiones.

## Correcciones al material del docx

- Usar `localhost:8000`, no 8080.
- Nacionalidad (radio) puede llegar vacía: leer con `request.POST.get(...)`, no con `[...]`.
- No dejar `// comentarios` dentro del HTML y no cerrar `<input>` con `</input>`.
- No mostrar la contraseña en la página de respuesta.
- Aceptar coma decimal (`2,15`) en el cilindro, o usar `type="number" step="any"`.

## Agentes (`.claude/agents/`)

- `django-dev`: implementa vistas, URLs y plantillas según las convenciones.
- `lab-reviewer`: revisa el trabajo contra la rúbrica y las correcciones del docx. No edita código.
- `doc-writer`: redacta la Actividad 1 y las conclusiones en `docs/`, con ortografía cuidada.

Las capturas pueden tomarse con el navegador integrado; el video lo graba el alumno.

## Convenciones

- Idioma: español para comunicación, comentarios, textos de UI y documentación.
- Nombres de apps, URLs y variables en español y `snake_case`, como en el docx.
- Cada app define `app_name` en su `urls.py` y las rutas llevan `name=`; en plantillas usar `{% url 'app:nombre' %}`.
- Plantillas en `<app>/templates/<app>/`.
- Todo formulario POST lleva `{% csrf_token %}`.
- Validar la entrada del usuario (campos vacíos, valores no numéricos, división o dominio inválido) y mostrar un mensaje de error en vez de fallar con 400/500.
- Las vistas pasan datos a la plantilla solo mediante `context`.
- Commits en español, uno por actividad o paso. Rama `master`.
- Mantener los cambios pequeños y enfocados en lo que se pida.
- Actualizar este archivo cuando cambie el stack, la estructura o las convenciones.
