class Fournisseur:
    def __init__(self, nom, contact, produits_fournis=None):
        self.nom = nom
        self.contact = contact
        self.produits_fournis = produits_fournis if produits_fournis else []

    def ajouter_produit(self, reference_produit):
        if reference_produit not in self.produits_fournis:
            self.produits_fournis.append(reference_produit)

    def to_dict(self):
        return {
            "contact": self.contact,
            "produits_fournis": self.produits_fournis
        }

    @classmethod
    def from_dict(cls, nom, data):
        return cls(
            nom=nom,
            contact=data["contact"],
            produits_fournis=data.get("produits_fournis", [])
        )