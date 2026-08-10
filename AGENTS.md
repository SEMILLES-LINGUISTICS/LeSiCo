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

## Convenciones de Git, Issues y Pull Requests

### Títulos de issues
- Todo el título se escribe en minúscula.
- Comienza con un prefijo en inglés y entre corchetes: `[feature]`, `[fix]`, `[docs]`, `[chore]` u otro equivalente.
- Formato: `"[prefijo] descripción breve"`
- Ejemplo: `"[feature] ajustar esquema de colores"`

### Commits
- Tipo de commit en minúscula: `feat:`, `fix:`, `docs:`, etc.
- Descripción en minúscula
- Ejemplo: `feat: esquema de colores brillante con L-S-C resaltadas`

### Pull Requests
- El título sigue el formato y el prefijo del issue; se mantiene completamente en minúscula.
- Body resume cambios, archivos modificados y verificación realizada
- Ejemplo: `"[feature] ajustar esquema de colores"`

### Ramas (branches)
- Formato: `feature/número-descripción-en-kebab-case`
- Ejemplo: `feature/5-esquema-colores-brillante`
