# Reporte de casos de prueba

**Script probado:** `src/regulon_summary_in_tsv.py`  
**Archivo de entrada:** `data/raw/NetworkRegulatorGene.tsv` (RegulonDB)  
**Ejecución desde:** raíz del proyecto

---

## Caso 1 — Archivo válido (caso feliz)

**Qué se prueba:** que el programa lee el archivo TSV, ignora líneas de comentario (`#`), convierte a CSV, valida los datos, calcula el resumen de regulones y escribe el archivo de salida correctamente.

**Comando:**
```
python src/regulon_summary_in_tsv.py data/raw/NetworkRegulatorGene.tsv results/tabla_regulones.csv
```

**Salida en consola:**
```
Total de errores encontrados: 20
Ver results/regulon_errors.csv para detalles.

Resumen de regulones generado exitosamente. Ver results/tabla_regulones.csv para detalles.
```

**Primeras filas del archivo de salida (`results/tabla_regulones.csv`):**

| TF    | Total genes regulados | Total genes activados | Total genes reprimidos | Tipo de regulacion |
|-------|----------------------:|----------------------:|-----------------------:|-------------------|
| CRP   | 587                   | 495                   | 141                    | Dual              |
| Nac   | 557                   | 190                   | 395                    | Dual              |
| Lrp   | 368                   | 188                   | 238                    | Dual              |
| FNR   | 327                   | 221                   | 123                    | Dual              |
| ppGpp | 308                   | 196                   | 114                    | Dual              |

**Total de reguladores incluidos:** 319

**¿Funciona correctamente?** Sí. El programa procesa el archivo completo, detecta errores de datos, genera el resumen ordenado por número total de genes regulados (descendente) y escribe el CSV de salida.

---

## Caso 2 — Validación de datos: efectos faltantes

**Qué se prueba:** que la función `validar_datos` detecta filas con valor `NaN` en la columna `Effect`, las reporta y las guarda en `results/regulon_errors.csv`.

**Comando:** mismo que el Caso 1.

**Salida en consola:**
```
Total de errores encontrados: 20
Ver results/regulon_errors.csv para detalles.
```

**Primeras filas del archivo `results/regulon_errors.csv`:**

| Index | Regulador | Gen regulado | Efecto | Error           |
|------:|-----------|--------------|--------|-----------------|
| 4708  | Rob       | lpxC         |        | Efecto faltante |
| 4999  | Fur       | mcbA         |        | Efecto faltante |
| 5005  | Fur       | ycgZ         |        | Efecto faltante |
| 5692  | IHF       | patA         |        | Efecto faltante |
| 6279  | NagC      | feoA         |        | Efecto faltante |

**Total de errores detectados:** 20 (todos del tipo "Efecto faltante")

**¿Funciona correctamente?** Sí. El programa identifica las inconsistencias, informa cuántas encontró y guarda el reporte de errores en CSV sin interrumpir el procesamiento general.

---

## Caso 3 — Filtro por número mínimo de genes (`--min_genes`)

**Qué se prueba:** que el argumento opcional `--min_genes` filtra correctamente los reguladores con menos genes que el umbral indicado.

### Subcaso 3a — `--min_genes 10`

**Comando:**
```
python src/regulon_summary_in_tsv.py data/raw/NetworkRegulatorGene.tsv results/tabla_regulones_10.csv --min_genes 10
```

**Salida en consola:**
```
Total de errores encontrados: 20
Ver results/regulon_errors.csv para detalles.

Filtrando reguladores con al menos 10 genes regulados...

Resumen de regulones generado exitosamente. Ver results/tabla_regulones_10.csv para detalles.
```

**Resultado:** 115 reguladores incluidos (de 319 totales).  
El TF con menor número de genes en la salida tiene exactamente 10 genes regulados.

| TF    | Total genes regulados | Tipo de regulacion |
|-------|----------------------:|-------------------|
| YjjQ  | 10                    | Repressor         |
| RstA  | 10                    | Dual              |
| CdaR  | 10                    | Activator         |

### Subcaso 3b — `--min_genes 50`

**Comando:**
```
python src/regulon_summary_in_tsv.py data/raw/NetworkRegulatorGene.tsv results/tabla_regulones_50.csv --min_genes 50
```

**Salida en consola:**
```
Filtrando reguladores con al menos 50 genes regulados...

Resumen de regulones generado exitosamente. Ver results/tabla_regulones_50.csv para detalles.
```

**Resultado:** 30 reguladores incluidos.

**¿Funciona correctamente?** Sí. El filtro se aplica correctamente en ambos subcasos. Sin `--min_genes`, se incluyen todos los reguladores (valor por defecto: 0).

---

## Caso 4 — Archivo de entrada no existe

**Qué se prueba:** que el programa maneja correctamente `FileNotFoundError` cuando la ruta del archivo de entrada es inválida.

**Comando:**
```
python src/regulon_summary_in_tsv.py data/raw/archivo_inexistente.tsv results/salida.csv
```

**Salida en consola:**
```
Error: Archivo no encontrado - data/raw/archivo_inexistente.tsv
```

**Código de salida:** 1

**¿Funciona correctamente?** Sí. El programa muestra un mensaje claro con la ruta problemática y termina de forma controlada con `exit(1)` sin continuar la ejecución.

---

## Caso 5 — Argumentos obligatorios faltantes

**Qué se prueba:** que `argparse` detecta cuando faltan los argumentos `input_file` y/o `output_file`, y que el bloque `try/except SystemExit` en `parse_arguments` maneja la salida de forma controlada.

**Comando:**
```
python src/regulon_summary_in_tsv.py
```

**Salida en consola:**
```
usage: regulon_summary_in_tsv.py [-h] [--min_genes MIN_GENES] input_file output_file
regulon_summary_in_tsv.py: error: the following arguments are required: input_file, output_file
Error al parsear argumentos: 2
```

**Código de salida:** 1

**¿Funciona correctamente?** Sí. `argparse` muestra el uso correcto del programa, indica qué argumentos faltan, y el programa termina con `exit(1)`.

---

## Resumen de casos

| # | Caso                             | Tipo      | Resultado |
|---|----------------------------------|-----------|-----------|
| 1 | Archivo válido (caso feliz)      | Correcto  | Pasa      |
| 2 | Validación: efectos faltantes    | Correcto  | Pasa      |
| 3a| Filtro `--min_genes 10`          | Correcto  | Pasa      |
| 3b| Filtro `--min_genes 50`          | Correcto  | Pasa      |
| 4 | Archivo no encontrado            | Error     | Pasa      |
| 5 | Argumentos obligatorios faltantes| Error     | Pasa      |

Todos los casos responden adecuadamente: los casos correctos producen los resultados esperados y los casos de error terminan de forma controlada con mensajes claros.
