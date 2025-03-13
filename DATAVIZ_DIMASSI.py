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


import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset nettoyé
df = pd.read_csv("dataset_marketing_dataviz_clean.csv")

# Sélectionner uniquement les colonnes numériques pour le calcul de la corrélation
numeric_df = df.select_dtypes(include=["number"])

# Calculer la matrice de corrélation sur les données numériques
correlation_matrix = numeric_df.corr()

# Configurer la taille de la figure pour la heatmap
plt.figure(figsize=(10, 8))

# Créer la heatmap avec annotation
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Personnaliser le graphique
plt.title("Heatmap des Corrélations", fontsize=16)
plt.tight_layout()

# Enregistrer la heatmap dans un fichier image
plt.savefig("heatmap_correlations.png", dpi=300)

# Afficher le graphique
plt.show()