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
from scipy.stats import linregress
from matplotlib.ticker import FuncFormatter

# Charger le dataset nettoyé
df = pd.read_csv("dataset_marketing_dataviz_clean.csv")

# Vérifier que les colonnes "Clicks" et "Conversions" existent
if "Clics" not in df.columns or "Conversions" not in df.columns:
    print("Les colonnes 'Clics' et 'Conversions' doivent être présentes dans le dataset.")
    exit()

# Calculer la régression linéaire et le coefficient de corrélation
regression = linregress(df["Clics"], df["Conversions"])
slope = regression.slope
intercept = regression.intercept
r_value = regression.rvalue
p_value = regression.pvalue

# Créer le scatterplot avec la droite de régression
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x="Clics", y="Conversions",
            scatter_kws={'s':80, 'alpha':0.7, 'edgecolor':'white'},
            line_kws={'color':'red', 'linewidth':2})

# Personnaliser le graphique
plt.title("Scatterplot : Clics vs Conversions", fontsize=16)
plt.xlabel("Clics", fontsize=14)
plt.ylabel("Conversions", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)

# Formater les axes pour afficher les valeurs en milliers (ex : 50k, 100k, ...)
formatter = FuncFormatter(lambda x, pos: f'{int(x/1000)}k' if x >= 1000 else f'{x}')
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

# Annoter le graphique avec des informations clés
plt.annotate(
    f"Corrélation: {r_value:.2f}\nPente: {slope:.2e}\nP-value: {p_value:.2g}",
    xy=(0.05, 0.85), xycoords="axes fraction", fontsize=12,
    bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5)
)

plt.tight_layout()

# Enregistrer le graphique
plt.savefig("scatterplot_clics_vs_conversions_annotated.png", dpi=300)

# Afficher le graphique
plt.show()
