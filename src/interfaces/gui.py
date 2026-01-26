import tkinter as tk
from tkinter import ttk, messagebox
from src.services.utils import ProduitIntrouvableError, StockInsuffisantError

class GUI:
    def __init__(self, stock_mgr, vente_mgr, fournisseur_mgr, rapport_mgr, alerte_mgr, excel_mgr):
        self.stock_mgr = stock_mgr
        self.vente_mgr = vente_mgr
        self.fournisseur_mgr = fournisseur_mgr
        self.rapport_mgr = rapport_mgr
        self.alerte_mgr = alerte_mgr
        self.excel_mgr = excel_mgr
        
        self.root = tk.Tk()
        self.root.title("Gestion de Stocks")
        self.root.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)
        
        self.tab_produits = ttk.Frame(tab_control)
        self.tab_ventes = ttk.Frame(tab_control)
        self.tab_alertes = ttk.Frame(tab_control)
        
        tab_control.add(self.tab_produits, text="Produits")
        tab_control.add(self.tab_ventes, text="Ventes")
        tab_control.add(self.tab_alertes, text="Alertes")
        
        tab_control.pack(expand=1, fill="both")
        
        self.setup_produits_tab()
        self.setup_ventes_tab()
        self.setup_alertes_tab()

    def setup_produits_tab(self):
        # Frame Formulaire
        form_frame = ttk.LabelFrame(self.tab_produits, text="Nouveau Produit")
        form_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(form_frame, text="Nom:").grid(row=0, column=0)
        self.entry_nom = ttk.Entry(form_frame)
        self.entry_nom.grid(row=0, column=1)
        
        ttk.Label(form_frame, text="Catégorie:").grid(row=0, column=2)
        self.entry_cat = ttk.Entry(form_frame)
        self.entry_cat.grid(row=0, column=3)
        
        ttk.Label(form_frame, text="Quantité:").grid(row=1, column=0)
        self.entry_qte = ttk.Entry(form_frame)
        self.entry_qte.grid(row=1, column=1)
        
        ttk.Label(form_frame, text="Prix:").grid(row=1, column=2)
        self.entry_prix = ttk.Entry(form_frame)
        self.entry_prix.grid(row=1, column=3)
        
        btn_add = ttk.Button(form_frame, text="Ajouter", command=self.ajouter_produit)
        btn_add.grid(row=2, column=1, pady=5)
        
        # Liste
        self.tree_produits = ttk.Treeview(self.tab_produits, columns=('ID', 'Nom', 'Cat', 'Qte', 'Prix'), show='headings')
        self.tree_produits.heading('ID', text='ID')
        self.tree_produits.heading('Nom', text='Nom')
        self.tree_produits.heading('Cat', text='Catégorie')
        self.tree_produits.heading('Qte', text='Quantité')
        self.tree_produits.heading('Prix', text='Prix')
        self.tree_produits.pack(fill="both", expand=True, padx=10, pady=5)
        
        btn_refresh = ttk.Button(self.tab_produits, text="Actualiser", command=self.refresh_produits)
        btn_refresh.pack()
        
        self.refresh_produits()

    def setup_ventes_tab(self):
        form_frame = ttk.LabelFrame(self.tab_ventes, text="Enregistrer Vente")
        form_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(form_frame, text="ID Produit:").grid(row=0, column=0)
        self.entry_vente_id = ttk.Entry(form_frame)
        self.entry_vente_id.grid(row=0, column=1)
        
        ttk.Label(form_frame, text="Quantité:").grid(row=0, column=2)
        self.entry_vente_qte = ttk.Entry(form_frame)
        self.entry_vente_qte.grid(row=0, column=3)
        
        btn_sell = ttk.Button(form_frame, text="Vendre", command=self.faire_vente)
        btn_sell.grid(row=1, column=1)

    def setup_alertes_tab(self):
        self.tree_alertes = ttk.Treeview(self.tab_alertes, columns=('Nom', 'ID', 'Reste'), show='headings')
        self.tree_alertes.heading('Nom', text='Nom')
        self.tree_alertes.heading('ID', text='ID')
        self.tree_alertes.heading('Reste', text='Quantité Restante')
        self.tree_alertes.pack(fill="both", expand=True, padx=10, pady=10)
        
        btn_check = ttk.Button(self.tab_alertes, text="Vérifier", command=self.refresh_alertes)
        btn_check.pack()

    def ajouter_produit(self):
        try:
            nom = self.entry_nom.get()
            cat = self.entry_cat.get()
            qte = int(self.entry_qte.get())
            prix = float(self.entry_prix.get())
            
            new_id = self.stock_mgr.ajouter_produit(nom, cat, qte, prix)
            messagebox.showinfo("Succès", f"Produit ajouté : {new_id}")
            self.refresh_produits()
        except ValueError:
            messagebox.showerror("Erreur", "Format invalide.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def refresh_produits(self):
        for item in self.tree_produits.get_children():
            self.tree_produits.delete(item)
        for p in self.stock_mgr.get_all_produits():
            self.tree_produits.insert('', 'end', values=(p.reference, p.nom, p.categorie, p.quantite, p.prix))

    def faire_vente(self):
        try:
            ref = self.entry_vente_id.get()
            qte = int(self.entry_vente_qte.get())
            total = self.vente_mgr.enregistrer_vente(ref, qte)
            messagebox.showinfo("Vente", f"Vente OK. Total: {total}€")
            self.refresh_produits()
            self.refresh_alertes()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def refresh_alertes(self):
        for item in self.tree_alertes.get_children():
            self.tree_alertes.delete(item)
        for p in self.alerte_mgr.get_produits_critiques():
            self.tree_alertes.insert('', 'end', values=(p.nom, p.reference, p.quantite))

    def lancer(self):
        self.root.mainloop()