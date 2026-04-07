# 🏏 Cricket Match Outcome Predictor

## 📌 Project Overview

This project predicts the winner of a cricket match using Machine Learning.
It uses past match data like teams, toss result, and venue to make predictions.

---

## 🚀 Features

* Predict match winner between two teams
* Uses historical match data (IPL, ODI, T20, Test)
* Simple and interactive web interface
* Shows prediction confidence percentage

---

## 🧠 Machine Learning Model

* Algorithm used: Random Forest
* Accuracy: ~63%
* Key features used:

  * Team Strength (based on past wins)
  * Strength Difference between teams
  * Toss impact

---

## 📊 Dataset

* 9000+ cricket matches
* Formats included:

  * IPL
  * ODI
  * T20
  * Test
* Extracted features:

  * Teams
  * Toss Winner
  * Venue
  * Match Result

---

## 🌐 Web Application

Users can:

* Select Team 1 and Team 2
* Choose toss winner
* Select match type and venue
* Get predicted winner instantly

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* HTML, CSS

---

## 📂 Project Structure

```
cricket-predictor/
│
├── app.py
├── model.pkl
├── team_strength.json
├── requirements.txt
└── templates/
    └── index.html
```

---

## ⚙️ How to Run Locally

1. Clone the repository

```
git clone https://github.com/your-username/cricket-predictor.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🌍 Live Demo

👉 Add your deployed link here (Render)

---

## 📈 Future Improvements

* Add player statistics
* Include weather and pitch data
* Improve accuracy using advanced models
* Use real-time match data

---

## 👨‍💻 Author

**Rishith Kulkarni**
CSE Student

---

## ⭐ Conclusion

This project shows how Machine Learning can be applied in sports prediction.
