from src.config import settings

class AlerteManager:
    def __init__(self, stock_manager):
        self.stock_manager = stock_manager
        self.seuil = settings.SEUIL_ALERTE_STOCK

    def set_seuil(self, nouveau_seuil):
        self.seuil = int(nouveau_seuil)

    def get_produits_critiques(self):
        """Retourne la liste des produits dont la quantité <= seuil."""
        produits = self.stock_manager.get_all_produits()
        critiques = [p for p in produits if p.quantite <= self.seuil]
        return critiques