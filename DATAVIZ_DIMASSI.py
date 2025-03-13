import pandas as pd

# Charger le dataset
df = pd.read_csv("dataset_marketing_dataviz.csv")

# Afficher les premières lignes pour inspecter le contenu
print("Aperçu du dataset :")
print(df.head())

# Afficher les informations générales (types de données, valeurs manquantes, etc.)
print("\nInformations sur le dataset :")
print(df.info())

# Afficher le nombre de valeurs manquantes par colonne
print("\nNombre de valeurs manquantes par colonne :")
print(df.isnull().sum())

# Supprimer les doublons
df = df.drop_duplicates()

# Gestion des valeurs manquantes
# Option 1 : Supprimer les lignes contenant des valeurs manquantes
df_clean = df.dropna()

# Option 2 (alternative) : Remplir les valeurs manquantes par une valeur, par exemple la moyenne pour des colonnes numériques
# df_clean = df.fillna(df.mean())

# Sauvegarder le dataset nettoyé dans un nouveau fichier CSV
df_clean.to_csv("dataset_marketing_dataviz_clean.csv", index=False)
print("\nLe dataset nettoyé a été sauvegardé sous 'dataset_marketing_dataviz_clean.csv'.")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Charger le dataset
df = pd.read_csv("dataset_marketing_dataviz_clean.csv")

# 2. Agréger les impressions par campagne
impressions_par_campagne = df.groupby("Campagne")["Impressions"].sum().reset_index()

# 3. Configurer la taille de la figure
plt.figure(figsize=(10, 6))

# 4. Créer un diagramme en barres
sns.barplot(data=impressions_par_campagne, x="Campagne", y="Impressions")

# 5. Personnaliser l'histogramme
plt.title("Histogramme des Impressions par Campagne")
plt.xlabel("Campagne")
plt.ylabel("Nombre total d'Impressions")
plt.xticks(rotation=45)
plt.tight_layout()

# 6. Enregistrer l’histogramme sous forme de fichier PNG
plt.savefig("histogram_impressions.png", dpi=300)  # dpi=300 pour une bonne résolution

# 7. Afficher l’histogramme
plt.show()




