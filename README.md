# pandas with  Fares Kacem Biochimie Applique 07 12 2025 
# Mohamed Sori Aissa 
# Kies Abir
# Khaouani Norhene
# Touileb Aya Fatima Zahra 

import pandas as pd
# Données : séquences ADN,Longueur,pourcentage de GC
data = {
    "séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
     "Longueur":[12, 12, 12, 10, 11, 10, 10],
     "pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# Création d'un Dataframe ( tableau pandas)
df = pd.DataFrame(data)
print("*********** création et affichage*********")

# Affichage du tableau 
print("Tableau des séquences ADN :")
print(df)
