from flask import Flask
from flask_cors import CORS

import routes
from models import db

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
    db.create_all()

routes.init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
