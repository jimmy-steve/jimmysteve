from flask import Flask
from controllers.home import home_blueprint

# Créer l'application Flask
app = Flask(__name__)

# Enregistrer le blueprint (contrôleur)
app.register_blueprint(home_blueprint)

# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=True)
