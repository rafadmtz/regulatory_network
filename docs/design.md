## Algoritmo — versión 1 y 2 (datos en el código)

- Crear una lista u otra estructura de reguladores (sin repeticiones).

- Recorrer todas las interacciones (líneas).
 - Para cada interacción:
   - Obtener el TF.
   - Obtener el gen.
   - Si el TF no está guardado en la lista de reguladores, guardarlo.
   - Si el gen no está en la lista de genes vinculados a cada regulador, almacenarlo junto con el efecto del TF sobre este gen.

   - Iterar sobre la lista de reguladores (TF). Ellos deben estar ordenados de forma alfabética.
    - Por cada TF:
     - Inicializar en 0 tres contadores: total de genes regulados, genes activados y genes reprimidos.
     - Analizar cada uno de los registros gen - efecto resguardados con anterioridad:
       - A medida que se recorren esos binomios, el total de genes regulados va incrementándose una unidad.
       - Si el efecto solo corresponde a '+', aumentar el total de genes activados; si solo aparece '-' en ese parámetro, elevar el total de genes reprimidos.
     - Interpretar los valores obtenidos: si ambos totales son mayores que cero, el TF tiene un efecto dual. En caso de que solo los genes activados rebasen a 0, el TF sería un activador; si el otro tipo de genes fuera el único total superior a 0, el TF sería un represor.
     - Imprimir 5 resultados: el nombre del TF, el número de genes regulados, el total de genes activados, la cantidad de genes reprimidos, y el tipo de efecto ejercido por el TF.

---

## Algoritmo — versión 3 (lectura desde archivo TSV)

El objetivo de esta versión es cambiar únicamente la fuente de los datos. El resto del programa (construcción del regulon y generación de salida) permanece igual.

### Pseudocódigo: obtener `interactions` desde el archivo

```
definir ruta del archivo

si el archivo no existe:
    mostrar mensaje de error
    terminar el programa

abrir el archivo
para cada línea del archivo:
    limpiar la línea (quitar espacios y saltos de línea)
    si la línea está vacía:
        ignorar y continuar
    si la línea empieza con "#":
        ignorar y continuar  (es un comentario)
    si la línea es el encabezado:
        ignorar y continuar
    separar la línea en columnas (dividir por tabulador)
    si el número de columnas es insuficiente:
        ignorar y continuar
    extraer TF (columna 2), gen (columna 5), efecto (columna 6)
    si efecto no es "+" ni "-":
        ignorar y continuar
    agregar (TF, gen, efecto) a interactions
cerrar el archivo
```

### Pseudocódigo: guardar resultados en archivo

```
crear directorio results/ si no existe
abrir archivo de salida en modo escritura
escribir encabezado (TF, total, activados, reprimidos, tipo, genes)
para cada TF en el regulon:
    construir la línea de resultado
    escribir la línea en el archivo
cerrar el archivo
```

### Decisiones de diseño

- **Índices fijos:** el programa usa posiciones fijas (columnas 2, 5 y 6) porque el formato del archivo de RegulonDB es estable y conocido. Esto simplifica el código, aunque lo hace dependiente del orden de columnas.
- **Descartar vs. fallar:** las líneas inválidas se descartan silenciosamente para que el programa procese el mayor número de datos posible sin interrumpirse.
- **Compatibilidad:** la lista `interactions` generada tiene el mismo formato que en las versiones anteriores: `[(TF, gen, efecto), ...]`. El resto del programa no requiere modificaciones.
