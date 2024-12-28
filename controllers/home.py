from flask import Blueprint, render_template
from models.model import Message  # Importer le modèle pour manipuler les données

# Crée un blueprint pour la page d'accueil
home_blueprint = Blueprint('home', __name__)


# Définir une route pour la page d'accueil
@home_blueprint.route('/')
def home():
    # Utilisation d'un modèle pour récupérer un message
    message = Message("Bienvenue sur la page d'accueil avec une navbar et un footer!")

    # Renvoyer le template 'home.html' et passer le message au template
    return render_template('home.html', message=message.get_content())
