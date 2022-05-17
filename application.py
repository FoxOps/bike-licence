# Partie Web

from flask import Flask, request, make_response, render_template
from main import bike_licence_info
import jinja2


loader = jinja2.FileSystemLoader('templates')

application = Flask(__name__)


@application.route("/", methods=["GET", "POST"])
def initialize():
    resp = make_response(render_template("answer_question.html"))
    return resp


@application.route("/start", methods=["GET", "POST"])
def start():
    reponse_formulaire = request.form.to_dict(flat=False)
    reponse_dictionnaire = {}

    for key, val in reponse_formulaire.items():
        reponse_dictionnaire[key] = val[0]

    reponses_pour_utilisateur, error = bike_licence_info(reponse_dictionnaire)

    resp = make_response(
        render_template("possibilite_permis.html",
                        reponses_pour_utilisateur=reponses_pour_utilisateur))

    return resp
