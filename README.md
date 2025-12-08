# pandas with  Fares Kacem Biochimie Appliquée 07 12 2025 
# Mohamed Sori Aissa 
# Kies Abir
# Khaouani Norhene
# Touileb Aya Fatima Zahra 

import pandas as pd
# Données : séquences ADN,Longueur,pourcentage de GC
data = {
    "séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
     "Longueur":[11, 12, 12, 10, 11, 10, 10],
     "pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# Création d'un Dataframe ( tableau pandas)
df = pd.DataFrame(data)
print("*********** création et affichage*********")

# Affichage du tableau 
print("Tableau des séquences ADN :")
print(df, "\n\n\n")
# Opération sur les tableaux:
imprimer ("********* Opérations *******")
#1) Sélectionner uniquement la colonne "longueur"
longueur = df [ "longueur" ]
imprimer ( longueur )

#2) Affichage avec une blibliothèque de visualisation (matplotlib)
#import matplotlib.pyplot as plt
#Données
#séquences = ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"]
#longueur =[11, 12, 12, 10, 11, 10, 10]
#gc_content = [50, 66.67, 58.33, 40, 45.45, 60, 50]
#Création d'un DataFrame
#data = {"Séquence": séquences,"Longueur": Longueur, "Pourcentage GC": gc_content}
#df = pd.DataFrame(données)

#3)Filtrer les séquences avec un pourcentage de GC supérieur à 50%
print( "************* Filtrage avec pourcentage %  *************" )
# Filtrer les séquences avec un pourcentage de GC supérieur à 50
filtred_df = df[df["Pourcntage GC"] > 50] 
print(filtred_df) 
