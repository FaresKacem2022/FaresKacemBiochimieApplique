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
# Création d'un Dataframe (tableau pandas)
df = pd.DataFrame(data)
print("*********** Création et affichage*********")

# Affichage du tableau 
print("Tableau des séquences ADN :")
print(df, "\n\n\n")
# Opération sur les tableaux:
print("********* Opérations *******")
#1) Sélectionner uniquement la colonne "longueur"
longueur = df["Longueur"]
print(longueur)

#2) Affichage avec une blibliothèque de visualisation (matplotlib)
#import matplotlib.pyplot as plt
#Données
#séquences = ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"]
#longueur =[11, 12, 12, 10, 11, 10, 10]
#gc_content = [50, 66.67, 58.33, 40, 45.45, 60, 50]
#Création d'un DataFrame
#data = {"Séquence": séquences,"Longueur": Longueur, "Pourcentage GC": gc_content}
#df = pd.DataFrame(données)

#3)Filtrer les séquences avec  longueur  supérieur à 10
print("************* Filtrage avec longueur  *************")
# Filtrer les séquences avec  longueur  supérieur à 10
filtered_df = df[df["Longueur"] > 10] 
print(filtered_df, "\n\n\n") 

#4)Calculer le pourcentage moyen de GC
print("******** Calcul de le pourcentage ********")
# Calculer la moyenne du pourcentage de GC
average_gc = df["pourcentage GC"].mean()
print(f"pourcentage moyen de GC : {average_gc:.3f}%", "\n\n\n")
#5)Ajouter d'une nouvelle colonne "catégorie GC"
df["Catégorie GC"]= df["pourcentage GC"].apply(lambda x: "Riche" if x > 55 else "Moyenne" if 45 < x < 55 else "Faible")
print(df, "\n\n\n")

#6)Ajouter une nouvelle colonne de nombre de G
print("***** Ajoute une nouvelle colonne de nombre de G *****")
# Ajouter une nouvelle colonne "nombre de G"
df["nombre de G"] = df["séquence"].apply(lambda séq: séq.count("G"))
print(df, "\n\n\n")

#7)Calculer l'écart-type de %GC et de la longueur des séquences
print("Écart-type pour 'pourcentage GC' et 'Longueur' :")
print(df[["pourcentage GC","Longueur"]].std())
#8) Sauvegarde et chargement des données avec panda
# Sauvegarder le DataFrame dans un fichier CSV
#df.to_csv("tableau_sequences.csv",index=False)
