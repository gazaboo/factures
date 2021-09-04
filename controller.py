# from flask import render_template, request
# from utils import get_info
# import pdfkit

# from server import app

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/form")
# def form():
#     return render_template("form.html")

# @app.route('/submit', methods=['POST'])
# def submit_facture():
#     infos = get_info(request.form)
#     output = render_template("facture_template.html", data=infos)
#     pdfkit.from_string(output, 'static/rendered/out.pdf', css= 'static/style.css',)     
#     return render_template("facture.html", data=infos)