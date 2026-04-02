# Guía de Flujo de Trabajo: DevSciLab Website

Esta guía documenta el ciclo de vida completo del desarrollo del sitio web, desde la edición en Flask hasta la generación del sitio estático final.

## 1. Desarrollo y Edición (Flask) -> `edit`

El sitio utiliza **Flask** para el desarrollo local. ¡La arquitectura actual usa Auto-Descubrimiento! Esto significa que **no necesitas modificar el archivo Python de código (`app.py`)** para agregar nuevas secciones.

*   **Páginas de Secciones Estáticas (HTML)**:
    *   Edita y crea principalmente los archivos en **Inglés** dentro de la carpeta (ej. `templates/nueva_pagina_en.html`).
    *   La estructura común (menú de navegación, pie de página) está centralizada en `templates/base.html`.
    *   Flask creará la ruta en vivo automáticamente `/<lang>/<nombre_pagina>/`.
*   **Páginas de Artículos/Blogs (Markdown)**:
    *   No necesitas HTML. Para crear una nueva publicación, ve a la carpeta `content/blog/` y crea un archivo `.md`.
    *   Al inicio de tu `.md`, usa el Frontmatter (metadatos) para definir formato:
        ```yaml
        title: "Mi Título"
        date: "2026-04-01"
        category: "Tecnología"
        lang: es
        ---
        Contenido...
        ```
    *   El Blog indexará estos artículos y sus categorías de forma autónoma.
*   **Comando de inicio local**:
    ```bash
    python app.py
    ```
*   **Visualización**: Abre tu navegador en `http://127.0.0.1:5000/`.

## 2. Traducción y Revisión -> `translate`

Una vez que has editado y finalizado una página, necesitas crear su contraparte en el otro idioma.

*   **Traducción de Páginas HTML (Automático)**:
    ```bash
    python translate_site.py templates/nombre_pagina_en.html
    ```
    *   *Resultado*: Generará/actualizará `templates/nombre_pagina_es.html`.
    *   *Revisión Manual (CRÍTICO)*: Revisa el `_es.html` resultante para pulir las frases desde el editor de código.

*   **Traducción de Artículos de Blog (Manual)**:
    *   Crea una copia del archivo `.md` (ej. cópialo y cámbiale nombre a `-es.md`).
    *   Asegúrate de cambiar la etiqueta dentro del archivo de `lang: en` a `lang: es` y traduce el texto directamente en el editor.

## 3. Generación de Sitio Estático -> `build`

Cuando todo el contenido de ambos idiomas esté aprobado, genera los archivos HTML estáticos y rutas dinámicas.

*   **Comando de generación**:
    ```bash
    python freeze.py
    ```
*   **Resultado**:
    *   Se crea o actualiza la carpeta `docs/` en la raíz del proyecto.
    *   Las plantillas descubiertas y los `.md` se estructuran en carpetas para soportar URLs limpias (ej: `docs/es/contact/index.html` o `docs/es/blog/category/tecnologia/index.html`).
*   **Prueba Final y Deploy**:
    *   Revisa tu carpeta `docs/` para ver el resultado limpio.
    *   Realiza un "git push" de la la rama para GitHub Pages (Sabiendo que GitHub leerá la carpeta de `docs/`).
