# Lista de interacciones en la red regulatoria. Cada tupla incluye el nombre del TF, su target gene, y el efecto sobre dicho gen.
interactions = [
("AraC", "araA", "+"),
("AraC", "araB", "-"),
("LexA", "recA", "-"),
("CRP", "lacZ", "+"),
("CRP", "lacY", "+")
]





tfs=[TF for TF, gene, effect in interactions]

regulon = {tf: [] for tf in tfs}  


for tf, gene, effect in interactions:
    regulon[tf].append((gene, effect))
    

print("Estructura del regulon:")
print(regulon)
print()

for tf in regulon:
    total_genes = len(regulon[tf])
    
    genes_activados = 0
    genes_reprimidos = 0
    
    for gene, effect in regulon[tf]:
        
        if effect == "+":
            genes_activados += 1
        elif effect == "-":
            genes_reprimidos += 1

    
    
    
    if genes_activados and genes_reprimidos:
        tipo_regulacion = "Dual"
    
    elif genes_activados:
        tipo_regulacion = "Activator"
    
    elif genes_reprimidos:
        tipo_regulacion = "Repressor"

    print(f"TF: {tf}")
    print(f"Total genes regulados: {total_genes}")
    print(f"Genes activados: {genes_activados}")
    print(f"Genes reprimidos: {genes_reprimidos}")
    print(f"Tipo de regulacion: {tipo_regulacion}")
    print()
    


