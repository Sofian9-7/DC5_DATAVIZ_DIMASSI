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

# Charger le dataset nettoyé (assurez-vous que 'Campaign' et 'Conversions' existent)
df = pd.read_csv("dataset_marketing_dataviz_clean.csv")

# Agréger les conversions par type de campagne
df_grouped = df.groupby("Campagne")["Conversions"].sum().reset_index()

# Créer une figure avec 2 sous-graphes côte à côte
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

### Version Honnête et Informative ###
# Barplot avec axe y débutant à 0
sns.barplot(data=df_grouped, x="Campagne", y="Conversions", ax=ax1, palette="viridis")
ax1.set_title("Version Honnête et Informative", fontsize=16)
ax1.set_xlabel("Type de Campagne", fontsize=14)
ax1.set_ylabel("Conversions", fontsize=14)
ax1.set_ylim(0, df_grouped["Conversions"].max() * 1.1)  # Axe y commençant à 0
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle="--", alpha=0.5)

### Version Trompeuse ###
# Même graphique mais avec axe y tronqué pour exagérer les différences
sns.barplot(data=df_grouped, x="Campagne", y="Conversions", ax=ax2, palette="viridis")
ax2.set_title("Version Trompeuse", fontsize=16)
ax2.set_xlabel("Type de Campagne", fontsize=14)
ax2.set_ylabel("Conversions", fontsize=14)
# On définit l'axe y en partant d'une valeur > 0, ici proche du minimum observé
y_min = df_grouped["Conversions"].min()
y_max = df_grouped["Conversions"].max()
ax2.set_ylim(y_min, y_max * 1.1)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, linestyle="--", alpha=0.5)

plt.suptitle("Comparaison des Visualisations : Conversions vs Type de Campagne", fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig("comparaison_conversions_campaign.png", dpi=300)
plt.show()
