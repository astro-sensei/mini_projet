# Documentation Utilisateur — Application de Gestion des Stocks

## Introduction
Cette application permet à une petite entreprise de gérer ses produits, ses ventes, ses fournisseurs, ses alertes de stock et ses fichiers de données.  
Elle propose deux modes d’utilisation :  
- une interface en ligne de commande (CLI)  
- une interface graphique (GUI) basée sur Tkinter  

Cette documentation explique comment utiliser l’application au quotidien.

---

## Lancement de l’application

### Depuis un terminal
Dans le dossier du projet :

```
python src/main.py
```

L’application vous propose alors de choisir entre :  
1. Interface console  
2. Interface graphique  

---

## Interface console (CLI)

L’interface console fonctionne sous forme de menus numérotés.  
Le menu principal propose :

```
1. Gestion des produits
2. Gestion des ventes
3. Gestion des fournisseurs
4. Rapports et statistiques
5. Import / Export Excel
6. Alertes de stock
7. Quitter
```

L’utilisateur saisit simplement le numéro correspondant à l’action souhaitée.

---

## Gestion des produits

### Ajouter un produit
L’application vous demande :
- le nom du produit  
- la catégorie  
- la quantité  
- le prix unitaire  

L’ID du produit est généré automatiquement :  
- il s’agit d’un nombre aléatoire à 12 chiffres  
- l’utilisateur ne le saisit jamais  
- l’ID est affiché après la création du produit  

Exemple :  
```
Produit ajouté avec succès.
ID généré : 482910374652
```

### Modifier un produit
Vous pouvez modifier :
- le nom  
- la catégorie  
- la quantité  
- le prix  

L’ID ne peut jamais être modifié.

### Supprimer un produit
Vous devez saisir l’ID du produit à supprimer.

### Rechercher un produit
Deux modes de recherche :
- par nom  
- par catégorie  

### Afficher les produits
Plusieurs affichages sont disponibles :
- par catégorie  
- par quantité  
- tri croissant ou décroissant  

---

## Gestion des ventes

### Enregistrer une vente
L’application vous demande :
- l’ID du produit  
- la quantité vendue  
- la date (ou date automatique)  

L’application :
- vérifie que le produit existe  
- vérifie que le stock est suffisant  
- met à jour automatiquement la quantité restante  
- calcule le montant total de la vente  

### Consulter les ventes
Vous pouvez afficher :
- toutes les ventes  
- les ventes d’une période donnée  

---

## Rapports et statistiques

Le menu des rapports permet d’obtenir :

### Produits en stock
- produits les plus en stock  
- produits les moins en stock  

### Produits les plus vendus
- globalement  
- sur une période donnée  

### Chiffre d’affaires
- chiffre d’affaires total  
- chiffre d’affaires par catégorie  

Les rapports sont affichés sous forme de tableaux lisibles.

---

## Gestion des fournisseurs

### Ajouter un fournisseur
L’application demande :
- le nom  
- le contact  
- la liste des produits fournis (facultatif au départ)  

### Modifier un fournisseur
Vous pouvez modifier :
- le nom  
- le contact  
- les produits associés  

### Supprimer un fournisseur
Vous devez saisir son nom.

### Associer un produit à un fournisseur
Vous devez saisir :
- l’ID du produit  
- le nom du fournisseur  

---

## Alertes de stock faible

L’application détecte automatiquement les produits dont la quantité est inférieure au seuil défini dans les paramètres.

Vous pouvez :
- afficher les produits en alerte  
- modifier le seuil d’alerte  

---

## Import / Export Excel

### Importer des données
Vous pouvez importer :
- des produits  
- des ventes  

L’application vérifie :
- la présence des colonnes obligatoires  
- la validité des valeurs  
- les doublons  

### Exporter des données
Vous pouvez exporter :
- les produits  
- les ventes  

Les fichiers sont enregistrés dans le dossier `data/`.

---

## Interface graphique (GUI)

L’interface graphique propose une utilisation plus intuitive.

### Fenêtre principale
Elle donne accès à :
- Produits  
- Ventes  
- Fournisseurs  
- Rapports  
- Import/Export  
- Alertes  

### Formulaires
Chaque action (ajout, modification, vente…) ouvre une fenêtre dédiée avec des champs à remplir.

### Tableaux
Les produits, ventes et fournisseurs sont affichés sous forme de tableaux :
- triables  
- filtrables  
- consultables facilement  

### Pop-ups
L’application utilise des fenêtres d’alerte pour :
- les erreurs  
- les confirmations  
- les alertes de stock  

---

## Sauvegarde des données

Les données sont automatiquement enregistrées dans :
- produits.json  
- ventes.json  
- fournisseurs.json  

La sauvegarde est effectuée après chaque modification.

---

## Réinitialisation des données

Pour repartir à zéro, il suffit de supprimer les fichiers JSON dans le dossier `data/`.  
Ils seront recréés automatiquement au prochain lancement.
