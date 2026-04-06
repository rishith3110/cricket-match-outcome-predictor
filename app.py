from flask import Flask, request, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# load files safely
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("team_strength.json") as f:
    team_strength = json.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        team1 = request.form["team1"]
        team2 = request.form["team2"]
        toss_choice = request.form["toss"]
        match_type = request.form["match_type"]
        venue = request.form["venue"]

        # convert toss
        toss = team1 if toss_choice == "Team1" else team2

        # strengths
        t1 = team_strength.get(team1, 0.5)
        t2 = team_strength.get(team2, 0.5)

        # features
        strength_diff = t1 - t2
        toss_feature = 1 if toss == team1 else 0

        features = np.array([[t1, t2, strength_diff, toss_feature]])

        pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0]

        result = team1 if pred == 1 else team2

        # ⚠️ IMPORTANT CHANGE (for progress bar UI)
        confidence = max(prob)

        return render_template("index.html", result=result, prob=confidence)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()