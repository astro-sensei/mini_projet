import json
import os
from src.services.utils import FichierCorrompuError

class DataManager:
    """Gère la persistance des données via des fichiers JSON."""

    @staticmethod
    def _charger_json(filepath, default_content):
        """Méthode interne pour charger un fichier JSON en toute sécurité."""
        if not os.path.exists(filepath):
            return default_content
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Attention : Le fichier {filepath} est corrompu ou vide. Création d'un nouveau fichier.")
            return default_content
        except Exception as e:
            raise FichierCorrompuError(f"Erreur lors de la lecture de {filepath} : {e}")

    @staticmethod
    def _sauvegarder_json(filepath, data):
        """Méthode interne pour écrire dans un fichier JSON."""
        try:
            # S'assurer que le dossier existe
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise FichierCorrompuError(f"Erreur lors de l'écriture de {filepath} : {e}")

    def charger_produits(self, filepath):
        return self._charger_json(filepath, {})

    def sauvegarder_produits(self, filepath, produits_data):
        self._sauvegarder_json(filepath, produits_data)

    def charger_ventes(self, filepath):
        return self._charger_json(filepath, [])

    def sauvegarder_ventes(self, filepath, ventes_data):
        self._sauvegarder_json(filepath, ventes_data)

    def charger_fournisseurs(self, filepath):
        return self._charger_json(filepath, {})

    def sauvegarder_fournisseurs(self, filepath, fournisseurs_data):
        self._sauvegarder_json(filepath, fournisseurs_data)