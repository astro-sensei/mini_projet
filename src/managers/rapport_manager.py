class RapportManager:
    def __init__(self, stock_manager, vente_manager):
        self.stock_manager = stock_manager
        self.vente_manager = vente_manager

    def produits_plus_en_stock(self, top_n=5):
        produits = self.stock_manager.get_all_produits()
        # Tri par quantité décroissante
        produits.sort(key=lambda x: x.quantite, reverse=True)
        return produits[:top_n]

    def produits_moins_en_stock(self, top_n=5):
        produits = self.stock_manager.get_all_produits()
        # Tri par quantité croissante
        produits.sort(key=lambda x: x.quantite)
        return produits[:top_n]

    def chiffre_affaires_total(self):
        total = 0.0
        ventes = self.vente_manager.get_historique_ventes()
        for v in ventes:
            try:
                p = self.stock_manager.get_produit(v.reference_produit)
                total += v.calculer_total(p.prix)
            except:
                continue # Si le produit a été supprimé entre temps
        return total

    def produits_plus_vendus(self, top_n=5):
        """Calcule les produits les plus vendus en volume."""
        compteur = {}
        ventes = self.vente_manager.get_historique_ventes()
        for v in ventes:
            compteur[v.reference_produit] = compteur.get(v.reference_produit, 0) + v.quantite
        
        # Trier le dictionnaire
        trie = sorted(compteur.items(), key=lambda item: item[1], reverse=True)
        
        resultat = []
        for ref, qte in trie[:top_n]:
            try:
                p = self.stock_manager.get_produit(ref)
                resultat.append((p.nom, qte))
            except:
                resultat.append((ref, qte))
        return resultat