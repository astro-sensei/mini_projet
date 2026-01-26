from datetime import datetime

# --- Exceptions Personnalisées ---
class ProduitIntrouvableError(Exception):
    pass

class StockInsuffisantError(Exception):
    pass

class FournisseurIntrouvableError(Exception):
    pass

class FormatInvalideError(Exception):
    pass

class FichierCorrompuError(Exception):
    pass

# --- Fonctions Utilitaires ---

def valider_entier_positif(valeur, nom_champ):
    """Vérifie si une valeur est un entier positif."""
    try:
        val = int(valeur)
        if val < 0:
            raise ValueError
        return val
    except ValueError:
        raise FormatInvalideError(f"Le champ '{nom_champ}' doit être un entier positif.")

def valider_flottant_positif(valeur, nom_champ):
    """Vérifie si une valeur est un float positif."""
    try:
        val = float(valeur)
        if val < 0:
            raise ValueError
        return val
    except ValueError:
        raise FormatInvalideError(f"Le champ '{nom_champ}' doit être un nombre positif.")

def format_date_str(date_obj):
    """Convertit un objet datetime en string YYYY-MM-DD."""
    return date_obj.strftime("%Y-%m-%d")

def parse_date(date_str):
    """Convertit un string YYYY-MM-DD en objet datetime."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise FormatInvalideError("Format de date invalide (attendu : YYYY-MM-DD).")