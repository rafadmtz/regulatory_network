# Lista de interacciones en la red regulatoria. Cada tupla incluye el nombre del TF, su target gene, y el efecto sobre dicho gen.
interactions = [
("AraC", "araA", "+"),
("AraC", "araB", "-"),
("LexA", "recA", "-"),
("CRP", "lacZ", "+"),
("CRP", "lacY", "+")
]




# Extraemos los TFs unicos de las interacciones para construir el regulon
tfs=[TF for TF, gene, effect in interactions]




# Creamos un diccionario para almacenar el regulon, donde cada TF es una clave y su valor es una lista de tuplas (gene, effect)
regulon = {tf: [] for tf in tfs}  





# Llenamos el regulon con las interacciones correspondientes
for tf, gene, effect in interactions:
    regulon[tf].append((gene, effect))
    



# Imprimimos la estructura del regulon y el resumen de cada TF
print("Estructura del regulon:")
print(regulon)
print()






# Para cada TF en el regulon, contamos el total de genes regulados
# Además, contamos cuántos genes son activados y cuántos son reprimidos
# Finalmente, clasificamos el tipo de regulación (activador, represor o dual) y mostramos un resumen para cada TF. 
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
    print(f"Genes regulados: {regulon[tf]}")
    print(f"Total genes regulados: {total_genes}")
    print(f"Genes activados: {genes_activados}")
    print(f"Genes reprimidos: {genes_reprimidos}")
    print(f"Tipo de regulacion: {tipo_regulacion}")
    print()


