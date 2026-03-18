# Regulatory Network

Programa en Python que analiza interacciones entre factores de transcripción (TF) y genes en una red de regulación genética.

## Descripción

A partir de una lista de interacciones con el formato `(TF, gen, efecto)`, el programa:

1. Construye un **resumen por TF** con el total de genes regulados y su lista ordenada.
2. **Clasifica cada TF** como activador, represor o dual según el tipo de efectos que ejerce.

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
│   ├── interactions_1.txt      # Caso 1: AraC (dual) + LexA (represor)
│   ├── interactions_2.txt      # Caso 2: CRP (activador)
│   ├── interactions_3.txt      # Caso 3: LexA (represor) + AraC (dual)
│   └── interactions_full.txt   # Caso completo: AraC + LexA + CRP
│
├── main.py                     # Punto de entrada del programa
├── README.md
└── pyproject.toml
```


## Formato de entrada

Cada interacción es una tupla de tres elementos:

| Campo  | Descripción                        | Ejemplo  |
|--------|------------------------------------|----------|
| TF     | Factor de transcripción            | `AraC`   |
| gen    | Gen regulado                       | `araA`   |
| efecto | Tipo de regulación (`+` o `-`)     | `+`      |

## Clasificación de TFs

| Tipo       | Condición                          |
|------------|------------------------------------|
| Activador  | Solo regula genes con `+`          |
| Represor   | Solo regula genes con `-`          |
| Dual       | Regula genes con `+` y con `-`     |

## Ejemplo de salida

Con las interacciones del caso completo:

```
TF: AraC
Genes regulados: [('araA', '+'), ('araB', '-')]
Total genes regulados: 2
Genes activados: 1
Genes reprimidos: 1
Tipo de regulacion: Dual

TF: CRP
Genes regulados: [('lacZ', '+'), ('lacY', '+')]
Total genes regulados: 2
Genes activados: 2
Genes reprimidos: 0
Tipo de regulacion: Activator

TF: LexA
Genes regulados: [('recA', '-')]
Total genes regulados: 1
Genes activados: 0
Genes reprimidos: 1
Tipo de regulacion: Repressor
```

## Casos de prueba

Los casos de prueba definidos y sus resultados están documentados en [`docs/test_cases.md`](docs/test_cases.md).
Los datos de cada caso se encuentran en la carpeta [`data/`](data/).

## Documentación

- **Contexto del problema**: [`docs/context.md`](docs/context.md)
- **Diseño del algoritmo**: [`docs/design.md`](docs/design.md)
- **Casos de prueba**: [`docs/test_cases.md`](docs/test_cases.md)
- **Uso de IA**: [`docs/ai_log.md`](docs/ai_log.md)


## Autor

Rafael Díaz Martínez
