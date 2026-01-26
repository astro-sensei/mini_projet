import sys
from src.services.utils import ProduitIntrouvableError, StockInsuffisantError, FormatInvalideError

class CLI:
    def __init__(self, stock_mgr, vente_mgr, fournisseur_mgr, rapport_mgr, alerte_mgr, excel_mgr):
        self.stock_mgr = stock_mgr
        self.vente_mgr = vente_mgr
        self.fournisseur_mgr = fournisseur_mgr
        self.rapport_mgr = rapport_mgr
        self.alerte_mgr = alerte_mgr
        self.excel_mgr = excel_mgr

    def lancer(self):
        while True:
            print("\n--- GESTION DE STOCKS (CLI) ---")
            print("1. Gestion des produits")
            print("2. Gestion des ventes")
            print("3. Gestion des fournisseurs")
            print("4. Rapports")
            print("5. Alertes")
            print("6. Import/Export Excel")
            print("7. Quitter")
            
            choix = input("Choix : ")
            
            if choix == "1":
                self.menu_produits()
            elif choix == "2":
                self.menu_ventes()
            elif choix == "3":
                self.menu_fournisseurs()
            elif choix == "4":
                self.menu_rapports()
            elif choix == "5":
                self.menu_alertes()
            elif choix == "6":
                self.menu_excel()
            elif choix == "7":
                print("Au revoir !")
                sys.exit()
            else:
                print("Choix invalide.")

    def menu_produits(self):
        print("\n-- PRODUITS --")
        print("1. Ajouter")
        print("2. Modifier")
        print("3. Supprimer")
        print("4. Afficher tout")
        print("5. Rechercher")
        c = input("Choix : ")
        
        try:
            if c == "1":
                nom = input("Nom : ")
                cat = input("Catégorie : ")
                qte = int(input("Quantité : "))
                prix = float(input("Prix : "))
                new_id = self.stock_mgr.ajouter_produit(nom, cat, qte, prix)
                print(f"Produit ajouté avec succès. ID : {new_id}")
                
            elif c == "2":
                ref = input("ID du produit : ")
                print("Laisser vide si pas de changement.")
                nom = input("Nouveau nom : ") or None
                cat = input("Nouvelle catégorie : ") or None
                q_str = input("Nouvelle quantité : ")
                p_str = input("Nouveau prix : ")
                qte = int(q_str) if q_str else None
                prix = float(p_str) if p_str else None
                
                self.stock_mgr.modifier_produit(ref, nom, cat, qte, prix)
                print("Produit modifié.")

            elif c == "3":
                ref = input("ID du produit à supprimer : ")
                self.stock_mgr.supprimer_produit(ref)
                print("Produit supprimé.")

            elif c == "4":
                prods = self.stock_mgr.get_all_produits()
                for p in prods:
                    print(p)

            elif c == "5":
                term = input("Recherche : ")
                res = self.stock_mgr.rechercher_produit(term)
                for p in res:
                    print(p)

        except Exception as e:
            print(f"Erreur : {e}")

    def menu_ventes(self):
        print("\n-- VENTES --")
        print("1. Enregistrer une vente")
        print("2. Historique")
        c = input("Choix : ")
        
        if c == "1":
            ref = input("ID Produit : ")
            try:
                qte = int(input("Quantité : "))
                total = self.vente_mgr.enregistrer_vente(ref, qte)
                print(f"Vente enregistrée. Total : {total}€")
            except Exception as e:
                print(f"Erreur vente : {e}")
        elif c == "2":
            ventes = self.vente_mgr.get_historique_ventes()
            for v in ventes:
                print(f"Produit: {v.reference_produit} | Qte: {v.quantite} | Date: {v.date_vente}")

    def menu_fournisseurs(self):
        print("\n-- FOURNISSEURS --")
        print("1. Ajouter")
        print("2. Liste")
        c = input("Choix : ")
        if c == "1":
            nom = input("Nom : ")
            contact = input("Contact : ")
            try:
                self.fournisseur_mgr.ajouter_fournisseur(nom, contact)
                print("Fournisseur ajouté.")
            except Exception as e:
                print(f"Erreur : {e}")
        elif c == "2":
            for f in self.fournisseur_mgr.get_all_fournisseurs():
                print(f"{f.nom} ({f.contact}) - Produits fournis : {len(f.produits_fournis)}")

    def menu_rapports(self):
        print(f"CA Total : {self.rapport_mgr.chiffre_affaires_total()}€")
        print("Top 3 ventes :", self.rapport_mgr.produits_plus_vendus(3))

    def menu_alertes(self):
        critiques = self.alerte_mgr.get_produits_critiques()
        print("\n-- ALERTE STOCK FAIBLE --")
        if not critiques:
            print("Aucun produit critique.")
        for p in critiques:
            print(f"ATTENTION : {p.nom} (Ref: {p.reference}) - Reste : {p.quantite}")

    def menu_excel(self):
        from src.config import settings
        print("1. Exporter Produits")
        c = input("Choix : ")
        if c == "1":
            try:
                prods = self.stock_mgr.get_all_produits()
                self.excel_mgr.exporter_produits(settings.PRODUITS_XLSX, prods)
                print(f"Exporté vers {settings.PRODUITS_XLSX}")
            except Exception as e:
                print(f"Erreur export : {e}")