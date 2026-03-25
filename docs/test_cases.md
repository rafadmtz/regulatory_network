# Casos de prueba

## Primera versión del programa

### Caso 1

- Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC  |  2 |  araA, araB |  
| LexA | 1  | recA |


- Resultados:
```
AraC 2 araA, araB
LexA 1 recA

```

¿Coinciden con la salida esperada? Sí.

<br>

### Caso 2

- Entrada:

```
interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]
```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| CRP  |  3 |  lacA, lacY, lacZ |  

- Resultados:
```
CRP 3 lacA, lacY, lacZ
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso 3

- Entrada:

```
interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]

```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC | 2 | araA, araE |  
| LexA | 2 | recA, umuC|

- Resultados:
```
AraC 2 araA, araE
LexA 2 recA, umuC
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso adicional mencionado al final de la clase

-Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

```

- Salida esperada:

| TF  |  Total de genes  | Lista de genes | 
|---|---|---|
| AraC |  2 |  araA, araB |  
|  CRP |  2  | lacY, lacZ |
| LexA |  1 | recA |  

- Resultados:
```
AraC 2 araA, araB
CRP 2 lacY, lacZ
LexA 1 recA
```

¿Coinciden con la salida esperada? Sí.

<br>

## Segunda versión del programa (extensión)


### Primer caso

- Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

- Salida esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| AraC  | 2 | 1 | 1| Dual |  
| LexA | 1  | 0 | 1 | Represor |


- Resultados:
```
AraC 2 1 1 Dual
LexA 1 0 1 Represor
```

¿Coinciden con la salida esperada? Sí.

<br>

### Segundo caso

- Entrada:

```
interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]
```

- Salida esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| CRP  |  3 | 3 | 0 | Activador |  

- Resultados:
```
CRP 3 3 0 Activador
```


¿Coinciden con la salida esperada? Sí.

<br>


### Tercer caso

- Entrada:

```
interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]

```

- Salida esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|
| AraC | 2 | 1 | 1 | Dual |  
| LexA | 2 | 0 | 2 | Represor |

- Resultados:
```
AraC 2 1 1 Dual
LexA 2 0 2 Represor
```


¿Coinciden con la salida esperada? Sí.

<br>

### Caso adicional

-Entrada:

```
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

```

- Salida esperada:

| TF  |  Total de genes  | Genes activados | Genes reprimidos | Tipo de efecto | 
|---|---|---|---|---|
| AraC |  2 |  1 | 1 |  Dual |  
|  CRP |  2  | 2 | 0 | Activador |
| LexA |  1 | 0 | 1 | Represor |  

- Resultados:
```
AraC 2 1 1 Dual
CRP 2 2 0 Activador
LexA 1 0 1 Represor
```

¿Coinciden con la salida esperada? Sí.

<br>

## Tercera versión del programa (lectura desde archivo TSV)

Esta sección cubre los nuevos casos de prueba para la funcionalidad de lectura de archivo, validación de datos y generación de salida.

---

### Caso 1 — Archivo válido (caso feliz)

**Condición:** el archivo existe y contiene datos con el formato esperado.

**Qué se prueba:** lectura línea por línea, limpieza, extracción de columnas, construcción de `interactions`.

**Comportamiento esperado:**
- el programa procesa el archivo sin errores
- construye correctamente la lista de interacciones
- el resto del programa puede usar esa lista sin modificarse
- se genera el archivo de salida en `results/`

---

### Caso 2 — Líneas de comentario

**Condición:** el archivo contiene líneas que comienzan con `#`.

**Qué se prueba:** que el programa distingue metadatos de datos reales.

**Comportamiento esperado:**
- esas líneas se ignoran completamente
- no se intentan separar en columnas
- no generan errores

---

### Caso 3 — Encabezado presente

**Condición:** el archivo contiene una línea con nombres de columnas (comienza con `1)regulatorId`).

**Qué se prueba:** que el encabezado no se procese como una interacción.

**Comportamiento esperado:**
- el encabezado se ignora
- no aparece como parte de `interactions`

---

### Caso 4 — Línea vacía

**Condición:** el archivo contiene una o más líneas vacías.

**Qué se prueba:** limpieza de entrada, manejo de líneas sin contenido.

**Comportamiento esperado:**
- las líneas vacías se ignoran
- no provocan errores
- no agregan elementos incorrectos a `interactions`

---

### Caso 5 — Valor inválido en `function`

**Condición:** una fila tiene un valor distinto de `+` o `-` en la columna de efecto (por ejemplo `-+` o `?`).

**Qué se prueba:** validación de contenido.

**Comportamiento esperado:**
- esa fila no se incluye en `interactions`
- el programa continúa con el resto del archivo

---

### Caso 6 — Número insuficiente de columnas

**Condición:** una fila tiene menos columnas de las necesarias.

**Qué se prueba:** validación de estructura antes de acceder a índices.

**Ejemplo de línea problemática:**
```
AraC    araA
```

**Comportamiento esperado:**
- esa línea se descarta
- el programa no falla con `IndexError`
- las demás líneas válidas siguen procesándose

---

### Caso 7 — Archivo no existe

**Condición:** la ruta del archivo es incorrecta o el archivo fue movido o eliminado.

**Qué se prueba:** manejo de error al abrir el archivo.

**Comportamiento esperado:**
- el programa muestra un mensaje claro
- termina de forma controlada con `exit(1)`
- no sigue ejecutándose como si el archivo existiera

**Salida esperada:**
```
Error: archivo no encontrado data/raw/NetworkRegulatorGene.tsv
```

---

### Caso 8 — Archivo sin permisos de lectura

**Condición:** el archivo existe pero el programa no tiene permisos para leerlo.

**Qué se prueba:** manejo de errores de acceso.

**Comportamiento esperado:**
- se informa claramente el problema
- el programa termina de forma controlada con `exit(1)`

---

### Caso 9 — Integración con el programa anterior

**Condición:** la lista `interactions` fue construida a partir del archivo TSV.

**Qué se prueba:** compatibilidad con el código previo.

**Comportamiento esperado:**
- el programa anterior sigue funcionando sin cambios importantes
- se obtienen para cada TF:
  - nombre del TF
  - total de genes regulados
  - número de genes activados
  - número de genes reprimidos
  - tipo de regulación (activador, represor o dual)

---

### Caso 10 — Archivo de salida generado

**Condición:** la ejecución termina correctamente.

**Qué se prueba:** escritura de resultados, consistencia del formato de salida.

**Comportamiento esperado:**
- se crea el archivo `results/regulon_summary.tsv`
- contiene la información esperada en el formato definido
- puede abrirse y revisarse después

**Ejemplo de salida:**
```
TF	Total genes	Activados	Reprimidos	Tipo	Lista de genes
AraC	2	1	1	Dual	araA, araB
```

---

### Caso 11 — Interacciones duplicadas

**Condición:** el archivo contiene dos filas idénticas.

**Qué se prueba:** si el programa conserva o elimina duplicados.

**Comportamiento esperado:**
- debe ser consistente con la decisión de diseño
- el alumno debe explicar qué comportamiento eligió y por qué

---

### Caso 12 — Columnas en diferente orden

**Condición:** el archivo conserva los mismos nombres de columna pero cambia su posición.

**Qué se prueba:** qué tan rígido o robusto es el diseño.

**Comportamiento esperado:**
- si el diseño depende de índices fijos → probablemente falle
- si usa nombres de columna → debería seguir funcionando