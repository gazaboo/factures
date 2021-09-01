import json
from utils import generate_facture

f = open('cours.json',)
data = json.load(f)
for promo in data:
    for module in data[promo]:
        dates = [(month, listes_dates) for month in data[promo][module]["dates"]
                                       for listes_dates in data[promo][module]["dates"][month]]
        generate_facture(nom_promo=promo,
                         nom_module=module,
                         date_cours=dates,
                         nbre_jours_prepa=data[promo][module]["nbre_jours_prepa"])