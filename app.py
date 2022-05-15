## Partie Web ##

from flask import Flask, request, make_response, render_template
from main import bike_licence_info
import jinja2


loader=jinja2.FileSystemLoader('templates')

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def initialize():
    resp = make_response(render_template("answer_question.html"))
    return resp


@app.route("/start", methods=["GET","POST"])
def start():
    reponse_formulaire = request.form.to_dict(flat=False)

    for key, val in reponse_formulaire.items():
        reponse_formulaire[key] = val[0]

    reponses_pour_utilisateur = bike_licence_info(reponse_formulaire)

    resp = make_response(render_template("possibilite_permis.html", reponses_pour_utilisateur=reponses_pour_utilisateur))

    return resp
