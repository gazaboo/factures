import jinja2
import datetime as dt
import pdfkit

def generate_facture(nom_promo, nom_module, date_cours, nbre_jours_prepa):
    data = {
        "name":"Florian Dadouchi",
        "nom_module": nom_module,
        "date_cours": date_cours,
        "prix_journalier":450, 
        "date_emission_facture":dt.datetime.today().strftime("%d-%m-%Y"),
        "qte":len(date_cours),
        "nbre_jour_prepa":nbre_jours_prepa, 
    }

    data["prix_preparation"] = data['nbre_jour_prepa']*data['prix_journalier']
    data["prix_total_animation"] = len(data["date_cours"])*data['prix_journalier']
    data["prix_total"] = data['prix_preparation'] + data['prix_total_animation']


    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./template"))
    t = env.get_template("facture_template.html") 
    output = t.render(data=data)
    nom_facture = f'./rendered/facture_{data["nom_module"]}_{data["date_emission_facture"]}'

    with open(f"{nom_facture}.html", "w") as result_file:
        result_file.write(output)

    pdfkit.from_file(f"{nom_facture}.html", f"{nom_facture}.pdf")
