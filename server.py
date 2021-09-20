from flask import Flask, render_template, request
from utils import get_info
import pdfkit
import os

# login_manager = LoginManager()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit_facture():
    infos = get_info(request.form)
    output = render_template("facture_template.html", data=infos)
    name = f'fdadouchi_facture_{infos.nom_promotion}_{infos.nom_module}'
    pdfkit.from_string(output, f'static/rendered/{name}.pdf', css= 'static/style.css',)     
    return render_template("facture.html", data=infos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))