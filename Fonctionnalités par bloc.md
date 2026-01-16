# Fonctionnalités à implémenter
## 1. Gestion des produits
- Ajouter un produit avec :
  - Nom
  - Référence unique
  - Quantité en stock
  - Prix unitaire
  - Catégorie
- Afficher la liste des produits :
  - Classés par catégorie
  - Ou classés par quantité
- Rechercher un produit :
  - Par nom
  - Ou par référence
- Modifier les informations d’un produit :
  - Quantité
  - Prix
  - Catégorie
  - Nom
- Supprimer un produit du stock
## 2. Suivi des ventes
- Enregistrer une vente :
  - Produit vendu
  - Quantité vendue
  - Date de la vente
- Mettre à jour automatiquement le stock après la vente
- Générer un rapport des ventes :
  - Produits les plus vendus
  - Chiffre d’affaires total
  - Statistiques diverses
## 3. Rapports et statistiques
- Produits les plus en stock
- Produits les moins en stock
- Produits les plus vendus sur une période donnée
- Chiffre d’affaires par catégorie de produit
## 4. Persistance des données
- Sauvegarder les données :
  - Produits → JSON ou CSV
  - Ventes → JSON ou CSV
- Charger automatiquement les données au démarrage de l’application
## 5. Interface utilisateur
- Interface en ligne de commande **ou**
- Interface graphique avec **Tkinter**
# Contraintes techniques
- Organisation du code en modules ou classes
- Gestion des erreurs :
  - Produit non trouvé
  - Quantité insuffisante pour une vente
  - Mauvais format d’entrée utilisateur
- Utilisation des bibliothèques standard :
  - `json`, `csv`, `datetime`, etc.
# Extensions (facultatif)
- Import/export Excel avec **openpyxl**
- Alerte stock faible
- Gestion des fournisseurs :
  - Nom
  - Contact
  - Produits fournis