# LeSiCo

Portal público de la Base de Datos Léxica de Referencia de la Lengua de Señas Colombiana (LSC): LeSiCo / SEMILLES.

## Estado

Esta primera estructura incorpora:

- Home responsive;
- páginas informativas provisionales;
- rutas para las colecciones general, analizada y especializada;
- colección analizada existente, integrada al portal;
- páginas provisionales para funcionalidades en preparación.

## Desarrollo local

No requiere instalar dependencias. Desde la raíz:

```powershell
python -m http.server 8000
```

Luego abre `http://localhost:8000`.

No abras directamente los HTML con `file://`: la colección analizada necesita un servidor local para cargar su JSON.

## Validación

```powershell
python scripts/validate_site.py
node --check assets/js/site.js
node --check colecciones/analizada/aplicacion.js
```

## Datos

Este repositorio solo admite datos aprobados para publicación. El Excel de trabajo, las bases SQLite, los enlaces privados y los scripts de transformación pertenecen al repositorio privado del pipeline.

## Documentación

- [Arquitectura inicial](docs/arquitectura.md)
- [Contenidos pendientes](docs/contenidos-pendientes.md)
- [Cómo contribuir](CONTRIBUTING.md)
- [Licenciamiento pendiente](LICENSING.md)
