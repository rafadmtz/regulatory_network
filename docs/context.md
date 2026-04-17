# Context

Este proyecto analiza una red de regulación genética.

Los datos contienen interacciones entre factores de transcripción (TF) y genes.



**Formato de los datos:**

TF gene effect

**Ejemplo**

AraC araA +
AraC araB -
LexA recA -

**Objetivo del programa**

A partir de una lista de interacciones, el programa genera un resumen por TF que indica:

- Total de genes regulados
- Lista de genes regulados (ordenada)
- Clasificación del TF como activador, represor o dual

**Clasificación de TFs:**

| Tipo de efecto | Regla |
|---|---|
| Activador | Solo tiene + |
| Represor | Solo posee - |
| Dual | Contiene + y - |

**Salida esperada:**

| TF | Total de genes | Genes activados | Genes reprimidos | Tipo de efecto |
|---|---|---|---|---|
| AraC | 2 | 1 | 1 | Dual |
| CRP | 2 | 2 | 0 | Activador |
| LexA | 1 | 0 | 1 | Represor |

## Actualización v1.2

Problema:
El programa depende de rutas fijas (hardcoded), lo que limita su reutilización.

## Nuevo requisito:
El programa debe recibir el archivo de entrada y salida desde la línea de comandos.

## Actualización v1.3

Problema:
El programa no permite filtrar los reguladores por número mínimo de genes.

Nuevo requisito:
El programa debe permitir filtrar los TFs mostrando solo aquellos que tengan al menos un número mínimo de genes, definido por el argumento `--min_genes`.