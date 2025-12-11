# pandas with  Fares Kacem Biochimie Appliquée 07 12 2025 
# Mohamed Sori Aissa 
# Kies Abir
# Khaouani Norhene
# Touileb Aya Fatima Zahra 

import pandas as pd
# Données : séquences ADN,Longueur,pourcentage de GC,Déscription
data = {
    "séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
     "Longueur":[11, 12, 12, 10, 11, 10, 10],
     "pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50],
     "Description":["Gène Cible 01", "Gène Cible 02", "Gène Cible 03", "Gène Cible 04", "Gène Candidat", "Gène Page", "Séquence consensus"]
}
# Création d'un Dataframe (tableau pandas)
df = pd.DataFrame(data)
print("************* Création et affichage *************")

# Affichage du tableau 
print("Tableau des séquences ADN :")
print(df, "\n\n\n")

# Opération sur les tableaux:
print("************ Opérations ************")
#1) Sélectionner uniquement la colonne "longueur"
longueur = df["Longueur"]
print(longueur, "\n\n\n")


#2) Affichage avec une blibliothèque de visualisation (matplotlib)
#import matplotlib.pyplot as plt
#Données
#séquences = ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"]
#longueur =[11, 12, 12, 10, 11, 10, 10]
#gc_content = [50, 66.67, 58.33, 40, 45.45, 60, 50]
#Description:["Gène Cible 01", "Gène Cible 02", "Gène Cible 03", "Gène Cible 04", "Gène Candidat", "Gène Page", "Séquence consensus"]
#Création d'un DataFrame
#data = {"Séquence": séquences,"Longueur": Longueur, "Pourcentage GC": gc_content, "Description": Description}
#df = pd.DataFrame(données)


#3)Filtrer les séquences avec  longueur  supérieur à 10
print("************ Filtrage avec longueur  ************")
# Filtrer les séquences avec  longueur  supérieur à 10
filtered_df = df[df["Longueur"] > 10] 
print(filtered_df, "\n\n\n") 


#4)Calculer le pourcentage moyen de GC
print("************ Calcul de pourcentage moyen ************")
# Calculer la moyenne du pourcentage de GC
average_gc = df["pourcentage GC"].mean()
print(f"pourcentage moyen de GC : {average_gc:.3f}%", "\n\n\n")


#5)Ajouter une nouvelle colonne "Catégorie GC"
# Ajouter une nouvelle colonne "Catégorie GC"
df["Catégorie GC"]= df["pourcentage GC"].apply(lambda x: "Riche" if x > 55 else "Moyenne" if 45 < x < 55 else "Faible")
print(df, "\n\n\n")


#6)Ajouter une nouvelle colonne de nombre de G
print("************ Ajoute une nouvelle colonne ************")
# Ajouter une nouvelle colonne "nombre de G"
df["nombre de G"] = df["séquence"].apply(lambda séq: séq.count("G"))
print(df, "\n\n\n")

#Calculer le pourcentage moyen de G
average_g = df["Longueur"].mean()
print(f"pourcentage moyen de G : {average_g:.2f}%", "\n\n\n")

#Ajouter une nouvelle colonne nombre de T
print("*********** Ajoute une nouvelle colonne **********")
#Ajouter une nouvelle colonne "nombre de T" 
df["nombre de T"] = df["séquence"].apply(lambda séq: séq.count("T"))
print(df, "\n\n\n")

#Calculer le pourcentage moyen de T
average_t = df["Longueur"].mean()
print(f"pourcentage moyen de T : {average_t:.2f}%","\n\n\n")

#Ajouter une nouvelle colonne nombre de C
print("*********** Ajoute une nouvelle colonne ***********")
#Ajouter une nouvelle colonne "nombre de C"
df["nombre de C"] = df["séquence"].apply(lambda séq: séq.count("C"))
print(df, "\n\n\n") 

#Calculer le pourcentage moyen de C 
average_c = df["Longueur"].mean()
print(f"pourcentage moyen de C : {average_c:.2f}%", "\n\n\n") 

#Ajouter une nouvelle colonne nombre de A
print("********** Ajoute une nouvelle colonne **********")
#Ajouter une nouvelle colonne "nombre de A"
df["nombre de A"] = df["séquence"].apply(lambda séq: séq.count("A"))
print(df, "\n\n\n")

#Calculer le pourcentage moyen de A
average_A = df["Longueur"].mean()
print(f"pourcentage moyen de A : {average_A:.2f}%", "\n\n\n")

#7) Calculer l'écart-type de pourcentage GC et de la longueur des séquences
print("*********** Calcule de l'écart-type du pourcentage  GC et de la longueur des séquences ***********")
print("Écart-type pour 'pourcentage GC' et 'Longueur' :")
# Calculer l'écart-type de pourcentage GC et de la longueur des séquences  
print(df[["pourcentage GC","Longueur"]].std(), "\n\n\n")

#7.1)Arrondir les valeur de l'écart-type 
print("*********** Arrondir les valeurs de l'écart-type ***********") 
# Arrondir les valeurs de l'écart-type 
print(df[["pourcentage GC", "Longueur"]].std().to_string(float_format="{:.2f}".format), "\n\n\n")


#8) Calculer la Moyenne de pourcentage GC et de la longueur des séquences 
print("*********** Calcule de la Moyenne  du pourcentage  GC et de la longueur des séquences ***********")
# Calculer la Moyenne du pourcentage GC et de la longueur des séquences 
colonnes_cibles= ["pourcentage GC", "Longueur"]
print(f"Moyenne des colonnes {colonnes_cibles} :")
print(df[colonnes_cibles].mean(), "\n\n\n")


#9)Ajouter une nouvelle colonne "Utilité"
print("*********** Ajout de nouvelle colonne Utilité ***********")
# Ajouter une nouvelle colonne "Utilité"
df["Utilité"]= df["nombre de G"].apply(lambda x: "Utile" if x > 2 else "Inutile")
print(df, "\n\n\n")


#10)Filtrage des séquences Utile 
print("************ Filtrage des séquences Utile ************")
# Filtrer les séquences  Utile 
filtred_df = df[df["Utilité"] == "Utile" ]
print(filtred_df, "\n\n\n")


#11)Ajouter une nouvelle colonne de température de fusion "Tm"
print("********** Ajoute une nouvelle colonne 'Tm' **********")
#Ajouter une nouvelle colonne "Température de fusion'Tm'"
df["Tm"]= df["séquence"].apply(lambda séq: 2*(séq.count("A") + séq.count("T")) + 4*(séq.count("G") + séq.count("C")))
print(df, "\n\n\n")


#12) Sauvegarde et chargement des données avec panda
#Sauvegarder le DataFrame dans un fichier CSV
#df.to_csv("tableau_sequences.csv", index=False)
