# Registro de uso de IA

Este archivo documenta las interacciones con herramientas de inteligencia artificial durante el desarrollo del proyecto.

## Interacción
Herramienta: Claude (Cowork / Claude Desktop)
Modo: DELEGATE

Tarea encomendada: Llenar la documentación del proyecto: los casos de prueba (`docs/casos_prueba.md`), el contexto (`docs/context.md`) y el `README.md`.

Lo que hizo la IA:
- Leyó el código existente en `src/regulon_summary.py` para entender la lógica del programa antes de documentar.
- Completó `docs/casos_prueba.md` con los tres casos de prueba de la actividad, incluyendo la entrada, la salida esperada y los resultados reales del programa.
- Escribió `README.md` con la descripción del proyecto, la estructura de carpetas, instrucciones de uso y referencias a la documentación.

Lo que no hizo la IA:
- No escribió ni modificó el código de análisis (`regulon_summary.py`), el cual fue escrito íntegramente por el autor del proyecto.
- No modificó el diseño del algoritmo (`design.md`), que también fue redactado por el autor.

---

## Interacción 2
Herramienta: Claude Code (claude-sonnet-4-6)
Modo: DELEGATE
Fecha: 2026-03-25

Tarea encomendada: Actualizar la documentación del proyecto para reflejar la nueva funcionalidad de lectura desde archivo TSV (tercera versión del programa).

Lo que hizo la IA:
- Leyó el archivo `data/raw/NetworkRegulatorGene.tsv` para obtener la versión, fecha, estructura de columnas y valores del campo `function`.
- Actualizó `README.md` con la nueva estructura del proyecto (`data/raw/`, `results/`), la descripción del flujo de lectura desde archivo, la tabla de columnas del TSV, el nuevo ejemplo de salida y la tabla de manejo de errores.
- Completó `data/README.md` con la versión del dataset (Release 14.5, fecha 03-04-2026), la tabla completa de columnas, los valores posibles de `function` y la cita bibliográfica.
- Agregó la sección "Tercera versión" a `docs/test_cases.md` con los 12 casos de prueba para la lectura de archivo (archivo válido, comentarios, encabezado, líneas vacías, efecto inválido, columnas insuficientes, archivo no existe, sin permisos, integración, salida generada, duplicados, columnas reordenadas).
- Agregó la sección "versión 3" a `docs/design.md` con el pseudocódigo para leer el archivo, construir `interactions` y guardar resultados, más una sección de decisiones de diseño.

Lo que no hizo la IA:
- No escribió ni modificó ningún código (`src/regulon_summary.py`, `src/regulon_summary_in_tsv.py, `main.py`), según instrucción explícita del autor.


