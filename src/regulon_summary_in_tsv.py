import pandas as pd
import os


filename = "data/raw/NetworkRegulatorGene.tsv"


# Verificar si el archivo existe
if not os.path.exists(filename):
    print(f"Error: archivo no encontrado {filename}")
    exit(1)


# Crear el directorio de resultados si no existe
output_file = "results/regulon_summary.tsv"
os.makedirs(os.path.dirname(output_file), exist_ok=True)



#Creae un archivo csv filtrado
def convertir_tsv_a_csv():
    with open(filename) as f_in, \
         open("data/NetworkRegulatorGene_clean.csv", "w") as f_out:
        for line in f_in:
            if not line.startswith("#"):
                f_out.write(line.replace("\t", ","))
        
convertir_tsv_a_csv()



# Cargar el archivo CSV filtrado
df= pd.read_csv("data/NetworkRegulatorGene_clean.csv")


# Seleccionar solo las columnas relevantes
regulon_df = df[["2)regulatorName", "5)regulatedName", "6)function"]]
regulon_df=regulon_df.rename(columns={"2)regulatorName": "TF", "5)regulatedName": "Gene", "6)function": "Effect"})


tabla_errores = []

# Validar los datos y reportar cualquier inconsistencia
for index, regulador, regulado, efecto in regulon_df.itertuples(index=True):
    
    if pd.isna(regulador):
        tabla_errores.append((index, regulador, regulado, efecto, "Regulador faltante"))
    
    if pd.isna(regulado):
        tabla_errores.append((index, regulador, regulado, efecto, "Gen regulado faltante"))
    
    if pd.isna(efecto):
        tabla_errores.append((index, regulador, regulado, efecto, "Efecto faltante"))
        
    elif efecto not in ["+", "-", "-+"]:
        tabla_errores.append((index, regulador, regulado, efecto, "Valor invalido"))


# Verificar si se encontraron errores
if tabla_errores:
    print(f"Total de errores encontrados: {len(tabla_errores)}")
    print("Ver results/regulon_errors.csv para detalles.")

# Crear un DataFrame para los errores encontrados
errores_df = pd.DataFrame(
    tabla_errores,
    columns=["Index", "Regulador", "Gen regulado", "Efecto", "Error"]
)


# Guardar la tabla de errores en un archivo CSV
errores_df.to_csv("results/regulon_errors.csv", index=False)


# Obtener la lista de reguladores únicos
transcription_factors = regulon_df["TF"].unique()


# Crear una tabla resumen para cada regulador
tabla_resumen = []


# Iterar sobre cada regulador y calcular el número de genes regulados, activados, reprimidos y el tipo de regulación
for tf in transcription_factors:
    
    tf_df = regulon_df[regulon_df["TF"] == tf]

    activated = (tf_df["Effect"] == "+").sum()
    repressed  = (tf_df["Effect"] == "-").sum()
    dual = (tf_df["Effect"] == "-+").sum()
    
    
    if activated and repressed:
        tipo = "Dual"
    elif activated:
        tipo = "Activator"
    elif repressed:
        tipo = "Repressor"
    
    
    genes = tf_df["Gene"].unique().tolist()
    
    tabla_resumen.append((
        tf,
        len(genes),
        activated+dual,
        repressed+dual,
        tipo,
        genes
    ))
    

# Crear un DataFrame a partir de la tabla resumen
df_regulon = pd.DataFrame(
    tabla_resumen,
    columns=[
        "TF",
        "Total genes regulados",
        "Total genes activados",
        "Total genes reprimidos",
        "Tipo de regulacion",
        "Genes regulados"
    ]
)



# Ordenar el DataFrame por el número total de genes regulados
df_regulon = df_regulon.sort_values("Total genes regulados", ascending=False)



# Guardar el resumen en un archivo CSV
df_regulon.to_csv("results/regulon_summary.csv", index=False)

print("\nResumen de regulones generado exitosamente. Ver results/regulon_summary.csv para detalles.")