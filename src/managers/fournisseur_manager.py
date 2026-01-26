from src.models.fournisseur import Fournisseur
from src.services.utils import FournisseurIntrouvableError
from src.config import settings

class FournisseurManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        raw_data = self.data_manager.charger_fournisseurs(settings.FOURNISSEURS_JSON)
        self.fournisseurs = {}
        for nom, data in raw_data.items():
            self.fournisseurs[nom] = Fournisseur.from_dict(nom, data)

    def ajouter_fournisseur(self, nom, contact):
        if nom in self.fournisseurs:
            raise ValueError("Ce fournisseur existe déjà.")
        self.fournisseurs[nom] = Fournisseur(nom, contact)
        self._sauvegarder()

    def modifier_fournisseur(self, nom, nouveau_contact=None):
        if nom not in self.fournisseurs:
            raise FournisseurIntrouvableError
        if nouveau_contact:
            self.fournisseurs[nom].contact = nouveau_contact
            self._sauvegarder()

    def supprimer_fournisseur(self, nom):
        if nom in self.fournisseurs:
            del self.fournisseurs[nom]
            self._sauvegarder()
        else:
            raise FournisseurIntrouvableError

    def associer_produit(self, nom_fournisseur, reference_produit):
        if nom_fournisseur not in self.fournisseurs:
            raise FournisseurIntrouvableError
        
        self.fournisseurs[nom_fournisseur].ajouter_produit(reference_produit)
        self._sauvegarder()

    def get_all_fournisseurs(self):
        return list(self.fournisseurs.values())

    def _sauvegarder(self):
        data_to_save = {f.nom: f.to_dict() for f in self.fournisseurs.values()}
        self.data_manager.sauvegarder_fournisseurs(settings.FOURNISSEURS_JSON, data_to_save)