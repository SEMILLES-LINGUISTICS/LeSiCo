# 0001 · Sitio estático organizado por colecciones

- Estado: propuesta implementada para revisión
- Fecha: 2026-08-05

## Decisión

Mantener un sitio estático sin framework y organizar LeSiCo como portal con colección general, analizada y especializada.

## Motivos

- el equipo actual puede mantener HTML, CSS y JavaScript;
- GitHub Pages cubre el despliegue;
- no existen todavía funciones que requieran un servidor de aplicación;
- las colecciones comparten modelo conceptual, pero tienen diferentes niveles de procesamiento.

## Consecuencias

- el pipeline debe producir archivos públicos pequeños y estables;
- las páginas repetidas requieren disciplina de mantenimiento;
- se reconsiderará un generador estático cuando el volumen de páginas editoriales lo justifique.
