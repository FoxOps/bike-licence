# Partie Web

from flask import Flask, request, make_response, render_template
from main import bike_licence_info
import jinja2
from datetime import date


loader = jinja2.FileSystemLoader('templates')

application = Flask(__name__)


@application.route("/", methods=["GET", "POST"])
def initialize():
    resp = make_response(render_template("answer_question.html"))
    return resp


@application.route("/start", methods=["GET", "POST"])
def start():
    reponse_formulaire = request.form.to_dict(flat=False)
    reponse_dictionnaire = {} # noqa
    reponse_dictionnaire['date_of_birth'] = \
        reponse_formulaire['date_of_birth'][0] \
        if reponse_formulaire.get('date_of_birth')[0] \
        else date.today().strftime("%d/%m/%Y")
    reponse_dictionnaire['permis_b'] = True \
        if reponse_formulaire.get('permis_b') else False
    reponse_dictionnaire['permis_a1'] = True\
        if reponse_formulaire.get('permis_a1') else False
    reponse_dictionnaire['permis_a2'] = True\
        if reponse_formulaire.get('permis_a2') else False
    reponse_dictionnaire['date_permis_a2'] = \
        reponse_formulaire['date_permis_a2'][0] \
        if reponse_formulaire.get('date_permis_a2')[0] \
        else date.today().strftime("%d/%m/%Y")

    reponses_pour_utilisateur, error = bike_licence_info(reponse_dictionnaire)

    resp = make_response(
        render_template("possibilite_permis.html",
                        reponses_pour_utilisateur=reponses_pour_utilisateur))

    return resp


if __name__ == '__maim__':
    application.run()
