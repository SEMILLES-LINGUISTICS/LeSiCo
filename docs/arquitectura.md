# Arquitectura inicial

## Principio

LeSiCo es un portal con varias colecciones que comparten navegación, lenguaje visual y reglas de reconocimiento.

```text
Home
├── Información
├── Cómo usar LeSiCo
├── Colección general
├── Colección analizada
├── Colección especializada
└── Aportar
```

## Tecnología

El sitio usa HTML, CSS y JavaScript estáticos y puede publicarse con GitHub Pages. No se incorpora un framework mientras el tamaño y la frecuencia de cambios no lo justifiquen.

## Datos

- `colecciones/analizada/catalogo.json` es una exportación pública, no la fuente de verdad.
- La colección general tendrá un índice liviano de ocurrencias y referencias.
- Las colecciones especializadas reutilizarán identificadores y entidades centrales.
- El repositorio privado transforma y valida los datos; este repositorio solo los presenta.

## Rutas estables

- `/` Home
- `/colecciones/general/`
- `/colecciones/analizada/`
- `/colecciones/especializada/`

Los cambios futuros deben preservar estas rutas o incorporar una redirección compatible.
