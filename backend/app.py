import os

import routes
from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

frontend_folder = os.path.join(os.getcwd(), "..", "frontend")
dist_folder = os.path.join(frontend_folder, "dist")


# Serve static files from the frontend folder
@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)


with app.app_context():
    db.create_all()

routes.init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
