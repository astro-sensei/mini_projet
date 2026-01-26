import sys
import os

# Ajustement du path pour que les imports fonctionnent depuis src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.data_manager import DataManager
from src.services.excel_manager import ExcelManager
from src.managers.stock_manager import StockManager
from src.managers.vente_manager import VenteManager
from src.managers.fournisseur_manager import FournisseurManager
from src.managers.rapport_manager import RapportManager
from src.managers.alerte_manager import AlerteManager
from src.interfaces.cli import CLI
from src.interfaces.gui import GUI

def main():
    # 1. Instanciation des services techniques
    data_manager = DataManager()
    excel_manager = ExcelManager()

    # 2. Instanciation des managers (Injection de dépendances)
    stock_manager = StockManager(data_manager)
    vente_manager = VenteManager(data_manager, stock_manager)
    fournisseur_manager = FournisseurManager(data_manager)
    rapport_manager = RapportManager(stock_manager, vente_manager)
    alerte_manager = AlerteManager(stock_manager)

    # 3. Choix de l'interface
    print("Choisissez l'interface :")
    print("1. Console (CLI)")
    print("2. Graphique (GUI)")
    choix = input("Votre choix : ")

    if choix == "1":
        app = CLI(stock_manager, vente_manager, fournisseur_manager, rapport_manager, alerte_manager, excel_manager)
        app.lancer()
    elif choix == "2":
        app = GUI(stock_manager, vente_manager, fournisseur_manager, rapport_manager, alerte_manager, excel_manager)
        app.lancer()
    else:
        print("Choix invalide. Fermeture.")

if __name__ == "__main__":
    main()