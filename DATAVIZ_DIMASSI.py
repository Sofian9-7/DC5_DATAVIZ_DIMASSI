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

# Charger le dataset nettoyé
df = pd.read_csv("dataset_marketing_dataviz_clean.csv")

# Convertir la colonne 'Date' en datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Agréger les clics par mois (regroupement par fin de mois)
clicks_by_month = df.groupby(pd.Grouper(key="Date", freq="M"))["Clics"].sum().reset_index()

# Configurer le graphique
plt.figure(figsize=(10, 5))
sns.barplot(data=clicks_by_month, x="Date", y="Clics", color="skyblue")

# Personnaliser le graphique
plt.title("Evolution des Clicks (par Mois)")
plt.xlabel("Mois")
plt.ylabel("Nombre de Clics")
plt.xticks(rotation=45)

plt.tight_layout()

# Enregistrer le graphique sous forme d'image
plt.savefig("evolution_clics_barchart.png", dpi=300)

# Afficher le graphique
plt.show()

