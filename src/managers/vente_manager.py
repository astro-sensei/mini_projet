from src.models.vente import Vente
from src.services.utils import StockInsuffisantError, ProduitIntrouvableError
from src.config import settings

class VenteManager:
    def __init__(self, data_manager, stock_manager):
        self.data_manager = data_manager
        self.stock_manager = stock_manager
        
        raw_data = self.data_manager.charger_ventes(settings.VENTES_JSON)
        self.ventes = [Vente.from_dict(v) for v in raw_data]

    def enregistrer_vente(self, reference_produit, quantite):
        # 1. Vérifier si le produit existe
        try:
            produit = self.stock_manager.get_produit(reference_produit)
        except ProduitIntrouvableError:
            raise ProduitIntrouvableError("Impossible de vendre : produit inconnu.")

        # 2. Vérifier le stock
        if produit.quantite < quantite:
            raise StockInsuffisantError(f"Stock insuffisant. Dispo: {produit.quantite}, Demandé: {quantite}")

        # 3. Créer la vente
        nouvelle_vente = Vente(reference_produit, quantite)
        self.ventes.append(nouvelle_vente)

        # 4. Mettre à jour le stock (via le stock_manager qui gère la sauvegarde produits)
        self.stock_manager.modifier_produit(reference_produit, quantite=produit.quantite - quantite)

        # 5. Sauvegarder les ventes
        self._sauvegarder()
        
        return nouvelle_vente.calculer_total(produit.prix)

    def get_historique_ventes(self):
        return self.ventes

    def _sauvegarder(self):
        data_to_save = [v.to_dict() for v in self.ventes]
        self.data_manager.sauvegarder_ventes(settings.VENTES_JSON, data_to_save)