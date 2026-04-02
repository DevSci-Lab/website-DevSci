# 🧪 Guía de Flujo de Trabajo Git - DevSci Lab

Este documento describe los pasos sagrados para trabajar en equipo en el sitio web de DevSci Lab sin sobrescribir el trabajo del otro.

**Regla de Oro:** 🚫 NUNCA trabajes directamente en la rama `main`.

---

## 🔄 Fase 1: Sincronización (Antes de empezar)
*Haz esto SIEMPRE que te sientes en la computadora, antes de escribir nada.*

1. **Viaja a la rama principal:**
   ```bash
   git checkout main
   ```

2. **Baja los últimos cambios de la nube:** Esto asegura que tengas lo que tu compañero subió ayer.
   ```bash
   git pull origin main
   ```

## 🌿 Fase 2: Creación de tu Rama (Tu espacio seguro)
Crea una rama paralela para tu tarea específica.

1. **Crea y muévete a la nueva rama:**

Nomenclatura recomendada: ```nombre/tarea-corta```

   - Ejemplos David: ```david/fix-navbar```, ```david/formulario-contacto```
   - Ejemplos Silvia: ```silvia/cambio-logo```, ```silvia/textos-home```

```git checkout -b nombre/nombre-de-tu-tarea```

## 💾 Fase 3: Trabajo y Guardado
Edita los archivos HTML, Markdown (para el blog), CSS o añade imágenes. Cuando termines por hoy:

1. Verifica qué archivos modificaste (Opcional): Verás en rojo lo que cambiaste.
    ```git status```

2. Prepara los archivos para guardar: El punto . significa "todo lo modificado".
    ```git add .```

3. Guarda tus cambios con un mensaje descriptivo: 
    ```git commit -m "Descripción breve de lo que hice"```

## 🚀 Fase 4: Subir a la Nube
Envía tu trabajo a GitHub para que el otro lo pueda ver.

1. Sube tu rama: ¡Ojo! No subas a main, sube a tu rama.
    ```git push origin nombre/nombre-de-tu-tarea```

## 🤝 Fase 5: Unir el trabajo (En el Navegador)
Ahora ve a GitHub.com para fusionar tu trabajo con el proyecto principal.

1. Ve al repositorio: https://github.com/DevSci-Lab/website-DevSci

2. Verás un botón amarillo: Compare & pull request. Haz clic.

3. Escribe un título y descripción de los cambios.

4. Asignación (Opcional): En la derecha, en "Reviewers", puedes etiquetar a tu compañero.

5. Clic en Create Pull Request.

6. Revisión: El compañero revisa que todo esté bien.

7. Clic en Merge pull request → Confirm merge.

8. (Opcional) Clic en Delete branch para limpiar.
   
## 🆘 ¿Qué hago si me equivoco?
- Si escribí ```git commit``` pero me equivoqué en el mensaje: No pasa nada, sigue adelante, es solo un mensaje.

- GitHub me dice que hay "Conflictos": Significa que ambos editaron la misma línea.

1. GitHub te dejará editar el archivo web.

2. Busca las marcas <<<<<<<, =======, >>>>>>>.

3. Borra las marcas y deja el código correcto.

4. Guarda (Commit merge).

-------------------------
DevSci Lab - Workflow v1.1