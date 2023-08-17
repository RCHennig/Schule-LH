from flask import Flask, render_template, request, session, redirect, url_for
import random
import time
import mysql.connector
#hallo
app = Flask(__name__)
app.secret_key = "your_secret_key"
TIME_LIMIT = 10

# Set up the MySQL connection
db_connection = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)
db_cursor = db_connection.cursor()

def start_new_round():
    session["target_number"] = random.randint(1, 100)
    session["start_time"] = time.time()

def save_score(player, score):
    sql = "INSERT INTO scores (player, score) VALUES (%s, %s)"
    values = (player, score)
    db_cursor.execute(sql, values)
    db_connection.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if "score" not in session:
        session["score"] = 0
    if "target_number" not in session or time.time() - session["start_time"] > TIME_LIMIT:
        start_new_round()

    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == session["target_number"]:
            session["message"] = "Congratulations! You guessed the correct number."
            player_name = "Player"  # You can customize this to take player's name as input
            save_score(player_name, session["score"])
            session["score"] += 10
            start_new_round()
        elif guess < session["target_number"]:
            session["message"] = "Try higher!"
            session["score"] -= 1
        else:
            session["message"] = "Try lower!"
            session["score"] -= 1

    return render_template("index.html", score=session["score"], message=session.get("message"))

@app.route("/scores")
def scores():
    sql = "SELECT player, score FROM scores ORDER BY score DESC"
    db_cursor.execute(sql)
    scores = db_cursor.fetchall()
    return render_template("scores.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
