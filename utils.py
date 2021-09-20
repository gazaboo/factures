import datetime as dt
from random import randint

def get_info(req):
    data = {
        "organisme": req.get("organisme"),
        "name":"Florian Dadouchi",
        "nom_module": req.get("nom_cours"),
        "date_cours": req.get("dates").split(","),
        "prix_journalier":450, 
        "date_emission_facture":dt.datetime.today().strftime("%d-%m-%Y"),
        "qte": len(req.get("dates").split(",")),
        "nbre_jour_prepa": float(req.get("nbre_jours_prepa")), 
        "webbrowser": True, 
        "num_facture": dt.datetime.today().strftime("%M%S%f"), 
        "nom_promotion": req.get("nom_promotion")
    }
    data["prix_preparation"] = data['nbre_jour_prepa']*data['prix_journalier']
    data["prix_total_animation"] = len(data["date_cours"])*data['prix_journalier']
    data["prix_total"] = data['prix_preparation'] + data['prix_total_animation']
    return data
