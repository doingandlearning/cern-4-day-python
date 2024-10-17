from flask import Flask, jsonify, render_template

app = Flask(__name__)  # convention - you can go off piste if you like

data = {
    "players": [
        {"name": "Sewald", "score": 2},
        {"name": "Marc", "score": 2},
        {"name": "Matthias", "score": 2},
        {"name": "Albane", "score": 2},
    ]
}

@app.route('/api/data', methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/")
def index():
    players = data["players"]
    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)
