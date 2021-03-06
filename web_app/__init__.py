# web_app/_init_.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.routes import routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") 

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(routes)
    return app

if __name__ == "_main_":
    my_app = create_app()
    my_app.run(debug=True)