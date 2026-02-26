from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_codes():
    with open("codes.json", "r") as f:
        return json.load(f)

@app.route("/api/codes")
def get_all_codes():
    return jsonify(load_codes())

@app.route("/api/codes/<game>")
def get_game_codes(game):
    data = load_codes()
    filtered = [x for x in data if x["game"].lower() == game.lower()]
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(debug=True)
