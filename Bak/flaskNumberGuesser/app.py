from flask import Flask, render_template, request, session, redirect, url_for
from pygame import mixer
import random
import time
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"
#TIME_LIMIT = 10

# Set up the MySQL connection
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="RealVM2021",
    database="PlayerData"
)
db_cursor = db_connection.cursor()

def start_new_round():
    session["target_number"] = random.randint(1, 100)

def start_new_game():
    session["score"]= 0
    session["guessScore"]=0
    start_new_round()

def save_score(player, score):
    sql = "INSERT INTO scores (player, score) VALUES (%s, %s)"
    values = (player, score)
    db_cursor.execute(sql, values)
    db_connection.commit()

@app.route("/play", methods=["GET", "POST"])

def game():
    mixer.music.set_volume(session["volume"])

    if "guessScore" not in session:
        session["guessScore"]=0
    if "score" not in session:
        session["score"] = 0
    if "target_number" not in session:
        session["message"]= "Runde Vorbei"
        #start_new_round()

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess == session["target_number"]:
            session["message"] = "Congratulations! You guessed the correct number."
            player_name = "Player"  # You can customize this to take player's name as input
            session["score"] += 10
            session["guessScore"] += 1
            if session["guessScore"]>1: #Anzahl der zu erratenden Zahlen pro Runde
                save_score(player_name, session["score"])
                start_new_game()
            else:
                start_new_round()
        elif guess < session["target_number"]:
            session["message"] = "Try higher!"
            session["score"] -= 1
        else:
            session["message"] = "Try lower!"
            session["score"] -= 1

    return render_template("game.html", score=session["score"], message=session.get("message"))

@app.route("/scores")
def scores():
    mixer.music.set_volume(session["volume"])
    sql = "SELECT player, score FROM scores ORDER BY score DESC"
    db_cursor.execute(sql)
    scores = db_cursor.fetchall()
    return render_template("scores.html", scores=scores)

@app.route("/")
def menu():
    mixer.init()
    mixer.music.load('./music/backgroundMusic.mp3')
    mixer.music.play(999)
    return render_template("menu.html")

@app.route("/endscreen", methods=["GET","POST"])
def endscreen():
    if request.method=="POST":
         playerName = int(request.form["playername"])

    return render_template("endscreen.html")

@app.route("/options")
def options():
    if "volume" not in session:
        session["volume"] = 0.5
    if request.method == 'POST':
        session["volume"] = float(request.form.get("audioVolume") // 100)
        mixer.music.set_volume(session["volume"])
        #print(session["volume"])
    return render_template("options.html", audioVolume=session["volume"])

if __name__ == "__main__":
    app.run(debug=True)
