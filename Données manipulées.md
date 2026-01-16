# 1. Données liées aux produits
Chaque produit contient :
- **Nom**
- **Référence unique** (ID produit)
- **Quantité en stock**
- **Prix unitaire**
- **Catégorie** (Alimentaire, Électronique, etc.)

Ces données sont utilisées pour :  
- l’affichage du stock  
- la recherche  
- la modification  
- la suppression  
- les rapports d’inventaire  

---

# 2. Données liées aux ventes
Chaque vente enregistre :
- **Référence du produit vendu**
- **Nom du produit** (optionnel mais pratique)
- **Quantité vendue**
- **Date de la vente**
- **Montant total de la vente** (calculé : quantité × prix unitaire)

Ces données servent à :  
- mettre à jour le stock  
- générer les rapports de ventes  
- calculer le chiffre d’affaires  

---

# 3. Données statistiques et rapports
Elles ne sont pas stockées directement mais **calculées à partir des produits et des ventes** :
- Produits les plus en stock  
- Produits les moins en stock  
- Produits les plus vendus  
- Chiffre d’affaires total  
- Chiffre d’affaires par catégorie  
- Ventes sur une période donnée  

---

# 4. Données persistantes (fichiers)
L’application doit sauvegarder et charger :

- **produits.json** ou **produits.csv**
- **ventes.json** ou **ventes.csv**

Ces fichiers contiennent toutes les données nécessaires pour restaurer l’état de l’application au démarrage.

---

# ⭐ (Optionnel) **5. Données supplémentaires si extensions activées**
### 📉 Alerte stock faible
- Seuil minimal par produit  
- Liste des produits en alerte  

### 🧑‍💼 Gestion des fournisseurs
- Nom du fournisseur  
- Contact  
- Liste des produits fournis  

### 📂 Import/Export Excel
- Données produits au format `.xlsx`  
- Données ventes au format `.xlsx`  
