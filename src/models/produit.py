class Produit:
    def __init__(self, reference, nom, categorie, quantite, prix):
        self.reference = str(reference)
        self.nom = nom
        self.categorie = categorie
        self.quantite = int(quantite)
        self.prix = float(prix)

    def modifier(self, nom=None, categorie=None, quantite=None, prix=None):
        if nom:
            self.nom = nom
        if categorie:
            self.categorie = categorie
        if quantite is not None:
            self.quantite = int(quantite)
        if prix is not None:
            self.prix = float(prix)

    def to_dict(self):
        """Sérialisation pour JSON."""
        return {
            "nom": self.nom,
            "categorie": self.categorie,
            "quantite": self.quantite,
            "prix": self.prix
        }

    @classmethod
    def from_dict(cls, reference, data):
        """Désérialisation depuis JSON."""
        return cls(
            reference=reference,
            nom=data["nom"],
            categorie=data["categorie"],
            quantite=data["quantite"],
            prix=data["prix"]
        )
    
    def __str__(self):
        return f"[{self.reference}] {self.nom} ({self.categorie}) - Qte: {self.quantite} - {self.prix}€"