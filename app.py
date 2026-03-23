from flask import Flask, render_template
from flask_cors import CORS
from database import init_db
from routes.lead_routes import lead_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(lead_bp)

@app.route("/")
def home():
    return render_template("dashboard.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)