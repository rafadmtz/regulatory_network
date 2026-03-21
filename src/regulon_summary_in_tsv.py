import pandas as pd



#Creae un archivo csv filtrado

def convertir_tsv_a_csv():
    with open("data/raw/NetworkRegulatorGene.tsv") as f_in, \
         open("data/NetworkRegulatorGene_clean.csv", "w") as f_out:
        for line in f_in:
            if not line.startswith("#"):
                f_out.write(line.replace("\t", ","))
        
convertir_tsv_a_csv()


df= pd.read_csv("data/NetworkRegulatorGene_clean.csv")






regulon_df = df[["2)regulatorName", "5)regulatedName", "6)function"]]



regulon_df=regulon_df.rename(columns={"2)regulatorName": "TF", "5)regulatedName": "Gene", "6)function": "Effect"})






for index, regulador, regulado, efecto in regulon_df.itertuples(index=True):
    
    if pd.isna(regulador):
        print(f"Advertencia: Regulador faltante en la fila {index}")
    
    if pd.isna(regulado):
        print(f"Advertencia: Gen regulado faltante en la fila {index}")
    
    if pd.isna(efecto):
        print(f"Advertencia: Efecto faltante en la fila {index}, para el regulador {regulador} y el gen {regulado}")
    elif efecto not in ["+", "-", "-+"]:
        print(f"Advertencia: Valor invalido en la fila {index}: {efecto}, para el regulador {regulador} y el gen {regulado}")
        









transcription_factors = regulon_df["TF"].unique()




tabla_resumen = []




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




df_regulon.to_csv("data/regulon_summary.csv", index=False)
    
