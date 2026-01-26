import os

# Définition des chemins absolus basés sur l'emplacement de ce fichier
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Chemins des fichiers de données
PRODUITS_JSON = os.path.join(DATA_DIR, "produits.json")
VENTES_JSON = os.path.join(DATA_DIR, "ventes.json")
FOURNISSEURS_JSON = os.path.join(DATA_DIR, "fournisseurs.json")

# Chemins pour Excel
PRODUITS_XLSX = os.path.join(DATA_DIR, "produits.xlsx")
VENTES_XLSX = os.path.join(DATA_DIR, "ventes.xlsx")

# Paramètres par défaut
SEUIL_ALERTE_STOCK = 5  