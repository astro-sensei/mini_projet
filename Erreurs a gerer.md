# 1. Erreurs liées aux produits
### Recherche et identification
- Produit non trouvé (par nom ou référence)
- Catégorie inexistante ou vide
### Stock et quantité
- Quantité négative lors de l’ajout ou modification
- Tentative de vente avec une quantité supérieure au stock disponible
- Tentative de suppression d’un produit inexistant
### Prix
- Prix unitaire négatif ou non valide
- Format incorrect (ex : texte au lieu d’un nombre)
# 2. Erreurs liées aux ventes
- Produit vendu introuvable
- Quantité vendue non disponible
- Quantité vendue invalide (0, négative, non numérique)
- Date de vente au mauvais format
- Vente impossible car stock insuffisant
# 3. Erreurs liées aux fichiers et à la persistance
- Fichier JSON/CSV introuvable au démarrage
- Fichier corrompu ou mal formaté
- Erreur de lecture (permissions, encodage…)
- Erreur d’écriture lors de la sauvegarde
- Données manquantes ou incohérentes dans les fichiers
# 4. Erreurs d’entrée utilisateur
- Saisie non numérique pour quantité ou prix
- Champs obligatoires laissés vides
- Mauvais format de commande (en mode console)
- Choix de menu invalide
- Format de date incorrect
# 5. Erreurs logiques ou système
- Division par zéro (ex : statistiques mal calculées)
- Liste vide lors de la génération d’un rapport
- Mauvaise manipulation d’index dans une liste
- Erreur de type (ex : comparer un string et un int)
- Exception non prévue lors de l’exécution
# (Optionnel) 6. Erreurs liées aux extensions
### Alerte stock faible
- Seuil d’alerte non valide (négatif ou non numérique)
### Fournisseurs
- Fournisseur introuvable
- Données fournisseur incomplètes
### Import/Export Excel
- Fichier Excel introuvable
- Format Excel incorrect
- Erreur openpyxl (lecture/écriture)