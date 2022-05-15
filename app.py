## Partie Web ##

from flask import Flask, request, make_response, render_template
from main import interactWith
import jinja2


loader=jinja2.FileSystemLoader('templates')

app = Flask(__name__)


@app.route("/play", methods=["GET","POST"])
def play():
    user = request.args.get('user')
    reponse_utilisateur = request.args.get('reponse')
    username = user.get("name") if isinstance(user, dict) else ""

    dict_reponse, joueur_debug = interactWith(f'"cookie": {username}, "input_reponse": {reponse_utilisateur}')
    resp = make_response(render_template("answer_question.html", dict_reponse=dict_reponse, joueur_debug=joueur_debug))

    return resp


@app.route("/start", methods=["GET", "POST"])
def start_play():
    reponse_utilisateur = {}
    username = request.form.get("userName")

    dict_reponse, joueur_debug = interactWith(f'"cookie": {username}, "input_reponse": {reponse_utilisateur}')
    resp = make_response(render_template("answer_question.html", dict_reponse=dict_reponse, joueur_debug=joueur_debug))

    return resp


@app.route("/", methods=["GET", "POST"])
def start_add_user():
    resp = make_response(render_template("add_user.html"))
    return resp