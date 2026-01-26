import random
from src.models.produit import Produit
from src.services.utils import ProduitIntrouvableError, FormatInvalideError
from src.config import settings

class StockManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        # Chargement des données au démarrage : dictionnaire {ref: Produit}
        raw_data = self.data_manager.charger_produits(settings.PRODUITS_JSON)
        self.produits = {}
        for ref, data in raw_data.items():
            self.produits[ref] = Produit.from_dict(ref, data)

    def generer_id_produit(self):
        """
        Génère un ID unique de 12 chiffres aléatoires.
        Règle métier stricte : pas de saisie utilisateur.
        """
        while True:
            # Génération d'une chaîne de 12 chiffres
            identifiant = "".join(str(random.randint(0, 9)) for _ in range(12))
            # Vérification de l'unicité
            if identifiant not in self.produits:
                return identifiant

    def ajouter_produit(self, nom, categorie, quantite, prix):
        # Validation basique
        if quantite < 0 or prix < 0:
            raise FormatInvalideError("Quantité et prix doivent être positifs.")
        
        identifiant = self.generer_id_produit()
        nouveau_produit = Produit(identifiant, nom, categorie, quantite, prix)
        
        self.produits[identifiant] = nouveau_produit
        self._sauvegarder()
        return identifiant

    def modifier_produit(self, reference, nom=None, categorie=None, quantite=None, prix=None):
        if reference not in self.produits:
            raise ProduitIntrouvableError(f"Le produit {reference} n'existe pas.")
        
        produit = self.produits[reference]
        produit.modifier(nom, categorie, quantite, prix)
        self._sauvegarder()

    def supprimer_produit(self, reference):
        if reference in self.produits:
            del self.produits[reference]
            self._sauvegarder()
        else:
            raise ProduitIntrouvableError("Impossible de supprimer : produit introuvable.")

    def rechercher_produit(self, terme):
        """Recherche par nom ou catégorie (insensible à la casse)."""
        terme = terme.lower()
        resultats = []
        for p in self.produits.values():
            if terme in p.nom.lower() or terme in p.categorie.lower():
                resultats.append(p)
        return resultats

    def get_produit(self, reference):
        if reference not in self.produits:
            raise ProduitIntrouvableError(f"Produit {reference} introuvable.")
        return self.produits[reference]

    def get_all_produits(self):
        return list(self.produits.values())

    def _sauvegarder(self):
        # Conversion des objets en dict pour le JSON
        data_to_save = {p.reference: p.to_dict() for p in self.produits.values()}
        self.data_manager.sauvegarder_produits(settings.PRODUITS_JSON, data_to_save)