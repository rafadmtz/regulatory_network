# Regulatory Network

Programa en Python que analiza interacciones entre factores de transcripción (TF) y genes en una red de regulación genética, a partir de datos reales descargados de RegulonDB.

## Descripción

El programa lee un archivo TSV con interacciones regulatorias, lo valida y construye un resumen por TF que indica:

1. **Total de genes regulados** y su lista.
2. **Clasificación del TF** como activador, represor o dual según el tipo de efectos que ejerce.

Los resultados se guardan en un archivo de salida en la carpeta `results/`.

## Estructura del proyecto

```
regulatory-network/
│
├── src/
│   └── regulon_summary.py      # Lógica principal del análisis
│
├── docs/
│   ├── context.md              # Contexto del problema y salida esperada
│   ├── design.md               # Algoritmo paso a paso
│   ├── test_cases.md           # Casos de prueba con resultados
│   └── ai_log.md               # Registro de uso de IA
│
├── data/
│   ├── raw/
│   │   └── NetworkRegulatorGene.tsv   # Datos reales de RegulonDB
│   ├── interactions_1.txt      # Caso 1: AraC (dual) + LexA (represor)
│   ├── interactions_2.txt      # Caso 2: CRP (activador)
│   ├── interactions_3.txt      # Caso 3: LexA (represor) + AraC (dual)
│   ├── interactions_full.txt   # Caso completo: AraC + LexA + CRP
│   └── README.md               # Documentación del dataset
│
├── results/
│   └── regulon_summary.tsv     # Archivo de salida generado por el programa
│
├── main.py                     # Punto de entrada del programa
├── README.md
└── pyproject.toml
```

## Fuente de datos

Los datos provienen de **RegulonDB** (release 14.5), una base de datos de regulación transcripcional en *E. coli* K-12.

- Sitio: [regulondb.ccg.unam.mx](https://regulondb.ccg.unam.mx/datasets)
- Sección: Regulatory Network → NetworkRegulatorGene
- Archivo: `data/raw/NetworkRegulatorGene.tsv`

## Formato de entrada

### Antes (datos en el código)

```python
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

### Ahora (datos desde archivo TSV)

```python
interactions = leer_archivo("data/raw/NetworkRegulatorGene.tsv")
```

El archivo TSV tiene las siguientes columnas relevantes:

| # | Columna          | Descripción                                      |
|---|------------------|--------------------------------------------------|
| 1 | regulatorId      | Identificador del regulador                      |
| 2 | regulatorName    | Nombre del TF (factor de transcripción)          |
| 3 | regulatorGeneName| Gen(es) que codifican para el TF                 |
| 4 | regulatedId      | Identificador del gen regulado                   |
| 5 | regulatedName    | Nombre del gen regulado                          |
| 6 | function         | Efecto regulatorio (`+`, `-`, `-+`, `?`)         |
| 7 | confidenceLevel  | Nivel de confianza (C, S, W, ?)                  |

El programa usa las columnas `regulatorName` (2), `regulatedName` (5) y `function` (6).

## Flujo del programa

```
archivo TSV → validar → interactions [(TF, gen, efecto)] → regulon → archivo de salida
```

1. Leer el archivo línea por línea
2. Ignorar comentarios (`#`) y encabezado
3. Ignorar líneas vacías o con columnas insuficientes
4. Extraer TF, gen y efecto; aceptar solo `+` o `-`
5. Construir `interactions = [(TF, gen, efecto), ...]`
6. Reutilizar la lógica existente para construir el regulon
7. Guardar resultados en `results/regulon_summary.tsv`

## Clasificación de TFs

| Tipo       | Condición                          |
|------------|------------------------------------|
| Activador  | Solo regula genes con `+`          |
| Represor   | Solo regula genes con `-`          |
| Dual       | Regula genes con `+` y con `-`     |

## Ejemplo de salida

Archivo `results/regulon_summary.tsv`:

```
TF	Total genes	Activados	Reprimidos	Tipo	Lista de genes
AraC	2	1	1	Dual	araA, araB
CRP	2	2	0	Activator	lacY, lacZ
LexA	1	0	1	Repressor	recA
```

## Casos de prueba

Los casos de prueba están documentados en [`docs/test_cases.md`](docs/test_cases.md) e incluyen:

### Casos de lectura y validación del archivo

| # | Condición                          | Comportamiento esperado                              |
|---|------------------------------------|------------------------------------------------------|
| 1 | Archivo válido                     | Se procesa sin errores, se genera salida             |
| 2 | Líneas de comentario (`#`)         | Se ignoran completamente                             |
| 3 | Encabezado presente                | Se ignora, no se procesa como interacción            |
| 4 | Línea vacía                        | Se ignora, no genera error                           |
| 5 | Efecto inválido (distinto de +/-)  | La fila se descarta, el programa continúa            |
| 6 | Columnas insuficientes             | La línea se descarta, no produce `IndexError`        |
| 7 | Archivo no existe                  | Mensaje de error claro, el programa termina          |
| 8 | Sin permisos de lectura            | Mensaje de error claro, el programa termina          |
| 9 | Integración con programa anterior  | `interactions` compatible, resultados correctos      |
| 10| Archivo de salida generado         | Se crea `results/regulon_summary.tsv` con formato correcto |
| 11| Interacciones duplicadas           | Comportamiento consistente con la decisión de diseño |
| 12| Columnas en diferente orden        | Depende de si el diseño usa índices fijos o nombres  |

### Casos del programa anterior (datos en código)

Los casos de la versión anterior siguen siendo válidos. Consultar [`docs/test_cases.md`](docs/test_cases.md).

## Manejo de errores

| Error                    | Causa                                   | Respuesta del programa                     |
|--------------------------|-----------------------------------------|--------------------------------------------|
| `FileNotFoundError`      | Ruta incorrecta o archivo eliminado     | Mensaje claro + `exit(1)`                  |
| `PermissionError`        | Sin permisos de lectura                 | Mensaje claro + `exit(1)`                  |
| Columnas insuficientes   | Fila malformada                         | La fila se descarta, continúa              |
| Efecto no válido         | Valor distinto de `+` o `-`            | La fila se descarta, continúa              |

## Documentación

- **Contexto del problema**: [`docs/context.md`](docs/context.md)
- **Diseño del algoritmo**: [`docs/design.md`](docs/design.md)
- **Casos de prueba**: [`docs/test_cases.md`](docs/test_cases.md)
- **Uso de IA**: [`docs/ai_log.md`](docs/ai_log.md)
- **Dataset**: [`data/README.md`](data/README.md)

## Autor

Rafael Díaz Martínez
