from datetime import datetime

class Vente:
    def __init__(self, reference_produit, quantite, date_vente=None):
        self.reference_produit = reference_produit
        self.quantite = int(quantite)
        if date_vente:
            if isinstance(date_vente, str):
                 self.date_vente = date_vente # On garde le format str ISO pour simplifier le JSON
            else:
                 self.date_vente = date_vente.strftime("%Y-%m-%d")
        else:
            self.date_vente = datetime.now().strftime("%Y-%m-%d")

    def calculer_total(self, prix_unitaire):
        return self.quantite * float(prix_unitaire)

    def to_dict(self):
        return {
            "reference_produit": self.reference_produit,
            "quantite": self.quantite,
            "date_vente": self.date_vente
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            reference_produit=data["reference_produit"],
            quantite=data["quantite"],
            date_vente=data["date_vente"]
        )