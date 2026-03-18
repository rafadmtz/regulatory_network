# Casos de prueba

## Caso 1

- Entrada:

```python
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]
```

- Salida esperada:

| TF   | Total de genes | Genes activados | Genes reprimidos | Tipo de efecto |
|------|----------------|-----------------|------------------|----------------|
| AraC | 2              | 1               | 1                | Dual           |
| LexA | 1              | 0               | 1                | Represor       |

- Resultados:

```
TF: AraC
Total genes regulados: 2
Genes activados: 1
Genes reprimidos: 1
Tipo de regulacion: Dual

TF: LexA
Total genes regulados: 1
Genes activados: 0
Genes reprimidos: 1
Tipo de regulacion: Repressor
```

¿Coinciden con la salida esperada? Sí.

<br>

## Caso 2

- Entrada:

```python
interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]
```

- Salida esperada:

| TF  | Total de genes | Genes activados | Genes reprimidos | Tipo de efecto |
|-----|----------------|-----------------|------------------|----------------|
| CRP | 3              | 3               | 0                | Activador      |

- Resultados:

```
TF: CRP
Total genes regulados: 3
Genes activados: 3
Genes reprimidos: 0
Tipo de regulacion: Activator
```

¿Coinciden con la salida esperada? Sí.

<br>

## Caso 3

- Entrada:

```python
interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]
```

- Salida esperada:

| TF   | Total de genes | Genes activados | Genes reprimidos | Tipo de efecto |
|------|----------------|-----------------|------------------|----------------|
| AraC | 2              | 1               | 1                | Dual           |
| LexA | 2              | 0               | 2                | Represor       |

- Resultados:

```
TF: LexA
Total genes regulados: 2
Genes activados: 0
Genes reprimidos: 2
Tipo de regulacion: Repressor

TF: AraC
Total genes regulados: 2
Genes activados: 1
Genes reprimidos: 1
Tipo de regulacion: Dual
```

¿Coinciden con la salida esperada? Sí.
