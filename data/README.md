# Dataset: Regulatory interactions (RegulonDB)

## Fuente
RegulonDB — [regulondb.ccg.unam.mx](https://regulondb.ccg.unam.mx/datasets)

Sección: Regulatory Network → NetworkRegulatorGene

## Archivo
`NetworkRegulatorGene.tsv`

## Versión
RegulonDB Release 14.5 (fecha del archivo: 03-04-2026)

## Formato
TSV (tab-separated values)

## Columnas del archivo

| # | Nombre             | Descripción                                                          |
|---|--------------------|----------------------------------------------------------------------|
| 1 | regulatorId        | Identificador del regulador                                          |
| 2 | regulatorName      | Nombre del factor de transcripción (TF)                              |
| 3 | regulatorGeneName  | Gen(es) que codifican para el TF                                     |
| 4 | regulatedId        | Identificador del gen regulado                                       |
| 5 | regulatedName      | Nombre del gen regulado                                              |
| 6 | function           | Efecto regulatorio del TF sobre el gen                              |
| 7 | confidenceLevel    | Nivel de confianza de la interacción (C=Confirmed, S=Strong, W=Weak, ?=Unknown) |

## Columnas utilizadas en este proyecto
- `regulatorName` (columna 2) → TF
- `regulatedName` (columna 5) → gen
- `function` (columna 6) → efecto

## Observaciones
- El archivo tiene encabezado con metadatos (líneas que comienzan con `#`)
- La primera línea de datos contiene los nombres de columnas (comienza con `1)regulatorId`)
- Tiene columnas adicionales que no se usan en este proyecto
- Solo se usarán tres columnas: regulatorName, regulatedName y function
- La columna `function` puede tener los siguientes valores:
  - `+` → activador
  - `-` → represor
  - `-+` → dual (el programa lo descarta; requiere que el efecto sea solo `+` o `-`)
  - `?` → desconocido (se descarta)
- El programa solo procesa filas con efecto `+` o `-`

## Licencia
RegulonDB es de uso libre para fines académicos y no comerciales.
Consultar: [términos y condiciones](https://regulondb.ccg.unam.mx/manual/aboutUs/terms-conditions)

## Cita
Heladia Salgado, Socorro Gama-Castro, et al., *RegulonDB v12.0: a comprehensive resource of transcriptional regulation in E. coli K-12*, Nucleic Acids Research, 2023, gkad1072. https://doi.org/10.1093/nar/gkad1072
