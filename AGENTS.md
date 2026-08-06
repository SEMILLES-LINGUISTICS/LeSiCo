# Convenciones de trabajo para Codex

## Alcance

Este es el repositorio público de LeSiCo. Contiene el sitio estático y únicamente datos aprobados para publicación.

## Reglas

- No agregues `Master.xlsx`, bases SQLite, respaldos, rutas locales o enlaces privados.
- Mantén HTML, CSS y JavaScript sin framework mientras no exista una decisión documentada que lo cambie.
- Conserva las rutas públicas y los enlaces profundos de la colección analizada.
- Todo contenido visible debe funcionar con teclado y en pantallas de 360 px o más.
- Los videos deben incluir título, subtítulos y alternativa textual cuando estén disponibles.
- No reproduzcas materiales de terceros si la política de la fuente solo permite citarlos o enlazarlos.
- Las páginas y textos provisionales deben indicarlo expresamente.

## Verificación

```powershell
python scripts/validate_site.py
node --check assets/js/site.js
node --check colecciones/analizada/aplicacion.js
```

Prueba además el Home y la colección analizada en escritorio y móvil antes de integrar.

## Entrega

Relaciona cada solicitud de cambio con un issue y resume archivos, pruebas, capturas y decisiones pendientes. No copies chats completos como documentación del proyecto.
