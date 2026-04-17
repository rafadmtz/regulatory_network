import pandas as pd
import os
import argparse

#Creae un archivo csv filtrado
def convertir_tsv_a_csv(filename):
    try:
        with open(filename) as f_in, \
             open("data/NetworkRegulatorGene_clean.csv", "w") as f_out:
            for line in f_in:
                if not line.startswith("#"):
                    f_out.write(line.replace("\t", ","))
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado - {filename}")
        exit(1)
    except PermissionError:
        print(f"Error: Permiso denegado al procesar el archivo: {filename}")
        exit(1)
    except OSError as e:
        print(f"Error al procesar el archivo: {e}")
        exit(1)

# Validar los datos y reportar cualquier inconsistencia

def validar_datos(regulon_df):

    tabla_errores = []

    #Verificar que no haya valores faltantes en la columna "Effect"
    no_effect = regulon_df[regulon_df["Effect"].isna()]
    if not no_effect.empty:
        for index, row in no_effect.iterrows():
            tabla_errores.append((
                index,
                row["TF"],
                row["Gene"],
                row["Effect"],
                "Efecto faltante"
            ))


    #Verificar que los valores en la columna "Effect" sean válidos
    invalid_effects = regulon_df[~regulon_df["Effect"].isin(["+", "-", "-+", None])]
    if not invalid_effects.empty:
        for index, row in invalid_effects.iterrows():
            tabla_errores.append((
                index,
                row["TF"],
                row["Gene"],
                row["Effect"],
                "Efecto inválido"
            ))


    #Verificar que no haya valores faltantes en la columna "TF"
    no_regulador = regulon_df[regulon_df["TF"].isna()]
    if not no_regulador.empty:
        for index, row in no_regulador.iterrows():
            tabla_errores.append((
                index,
                row["TF"],
                row["Gene"],
                row["Effect"],
                "Regulador faltante"
            ))


    #Verificar que no haya valores faltantes en la columna "Gene"
    no_regulados = regulon_df[regulon_df["Gene"].isna()]
    if not no_regulados.empty:
        for index, row in no_regulados.iterrows():
            tabla_errores.append((
                index,
                row["TF"],
                row["Gene"],
                row["Effect"],
                "Gen regulado faltante"
            ))


        # Verificar si se encontraron errores
    if tabla_errores:
        print(f"\nTotal de errores encontrados: {len(tabla_errores)}")
        print("Ver results/regulon_errors.csv para detalles.")

        # Crear un DataFrame para los errores encontrados
        errores_df = pd.DataFrame(
        tabla_errores,
        columns=["Index", "Regulador", "Gen regulado", "Efecto", "Error"]
        )

        # Guardar la tabla de errores en un archivo CSV
        errores_df.to_csv("results/regulon_errors.csv", index=False)

    else:
        print("No se encontraron errores en los datos.")

    return tabla_errores



# Iterar sobre cada regulador y calcular el número de genes regulados, activados, reprimidos y el tipo de regulación
def calcular_resumen_regulon(regulon_df, transcription_factors, min_genes):

    if (min_genes):
        print(f"\nFiltrando reguladores con al menos {min_genes} genes regulados...")

    tabla_resumen = []

    for tf in transcription_factors:
        tf_df = regulon_df[regulon_df["TF"] == tf]

        genes = tf_df["Gene"].unique().tolist()
        
        if(len(genes) >= min_genes):
        
            activated = (tf_df["Effect"] == "+").sum()
            repressed  = (tf_df["Effect"] == "-").sum()
            dual = (tf_df["Effect"] == "-+").sum()


            if activated and repressed:
                tipo = "Dual"
            elif activated:
                tipo = "Activator"
            elif repressed:
                tipo = "Repressor"
            
            tabla_resumen.append((
                tf,
                len(genes),
                activated+dual,
                repressed+dual,
                tipo,
                genes
            ))

    return tabla_resumen


def parse_arguments():
    parser = argparse.ArgumentParser(description="Procesa regulones")
    parser.add_argument("input_file", help="Archivo de entrada, formato TSV")
    parser.add_argument("output_file", help="Archivo de salida, formato CSV")
    parser.add_argument("--min_genes", type=int, default=0, help="Número mínimo de genes regulados para incluir en el resumen")
    
    return parser.parse_args()
    




def main():
    
    """_summary_
    
    """
    
    #Crear un parser de argumentos para manejar la entrada y salida de archivos
    args = parse_arguments()

    # Crear el directorio de resultados si no existe"
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    
    # Verificar si el archivo existe y pasar a csv
    convertir_tsv_a_csv(args.input_file)

    try:
        df = pd.read_csv("data/NetworkRegulatorGene_clean.csv")
    except pd.errors.EmptyDataError:
        print("Error: el archivo CSV generado está vacío o no contiene columnas válidas.")
        exit(1)

    # Seleccionar solo las columnas relevantes
    regulon_df = df[["2)regulatorName", "5)regulatedName", "6)function"]]
    regulon_df = regulon_df.rename(columns={"2)regulatorName": "TF", "5)regulatedName": "Gene", "6)function": "Effect"})

    # Validar los datos y reportar cualquier inconsistencia mediante la funcion validar_datos
    validar_datos(regulon_df)

    # Obtener la lista de reguladores únicos
    transcription_factors = regulon_df["TF"].unique()

    tabla_resumen = calcular_resumen_regulon(regulon_df, transcription_factors, args.min_genes)

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
    df_regulon.to_csv(args.output_file, index=False)

    print(f"\nResumen de regulones generado exitosamente. Ver {args.output_file} para detalles.")


if __name__ == "__main__":
    main()
