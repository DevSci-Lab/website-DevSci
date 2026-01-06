# Guía de Flujo de Trabajo: DevSciLab Website

Esta guía documenta el ciclo de vida completo del desarrollo del sitio web, desde la edición en Flask hasta la generación del sitio estático final.

## 1. Desarrollo y Edición (Flask) -> `edit`

El sitio utiliza **Flask** para el desarrollo local. Esto permite usar plantillas (Jinja2) para evitar código repetido (como encabezados y pies de página).

*   **Archivos a editar**:
    *   Edita principalmente los archivos en **Inglés** (`templates/*_en.html`).
    *   La estructura común (menú, footer) está en `templates/base.html`.
*   **Comando de inicio**:
    ```bash
    python app.py
    ```
*   **Visualización**: Abre tu navegador en `http://127.0.0.1:5000/`.

## 2. Traducción Automática y Revisión -> `translate`

Una vez que has editado y finalizado una página en inglés, utiliza el script de traducción para generar la versión en español.

*   **Comando de traducción**:
    ```bash
    python translate_site.py templates/nombre_pagina_en.html
    ```
    *Ejemplo:* `python translate_site.py templates/researchers_en.html`
*   **Resultado**: Se generará o actualizará `templates/researchers_es.html`.
*   **Revisión Manual (CRÍTICO)**:
    *   La traducción automática no es perfecta.
    *   Abre el archivo generado (`templates/*_es.html`) en tu editor.
    *   Corrige textos, ajusta el tono y verifica que el formato HTML no se haya roto.
    *   Refresca el navegador local (`http://127.0.0.1:5000/researchers_es.html`) para verificar.

## 3. Generación de Sitio Estático -> `build`

Cuando todo el contenido (Inglés y Español) esté revisado y aprobado, genera los archivos HTML estáticos para subir a producción (GitHub Pages).

*   **Comando de generación**:
    ```bash
    python freeze.py
    ```
*   **Resultado**:
    *   Se crea una carpeta `build/` en la raíz del proyecto.
    *   Esta carpeta contiene el sitio web completo y estático.
*   **Prueba Final**:
    *   Abre el archivo `build/index.html` en tu navegador para una última verificación visual.
    *   Sube el contenido de la carpeta `build/` (o todo el repo, según tu configuración de deploy) a GitHub.
