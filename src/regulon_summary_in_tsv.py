import pandas as pd



#Creae un archivo csv filtrado

def convertir_tsv_a_csv():
    with open("data/raw/NetworkRegulatorGene.tsv") as f_in, \
         open("data/NetworkRegulatorGene_clean.csv", "w") as f_out:
        for line in f_in:
            if not line.startswith("#"):
                f_out.write(line.replace("\t", ","))
        

df= pd.read_csv("data/NetworkRegulatorGene_clean.csv")


regulon_df = df[["2)regulatorName", "5)regulatedName", "6)function"]]

regulon_df=regulon_df.rename(columns={"2)regulatorName": "TF", "5)regulatedName": "Gene", "6)function": "Effect"})

print(regulon_df.head())



