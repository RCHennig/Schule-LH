from flask import Flask, render_template, request, session, redirect, url_for
import random
import time

app = Flask(__name__)
app.secret_key = "your_secret_key"
TIME_LIMIT = 10  # Time limit for each guess in seconds

def start_new_round():
    session["target_number"] = random.randint(1, 100)
    session["start_time"] = time.time()

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
            session["score"] += 10
            start_new_round()
        elif guess < session["target_number"]:
            session["message"] = "Try higher!"
            session["score"] -= 1
        else:
            session["message"] = "Try lower!"
            session["score"] -= 1

    return render_template("index.html", score=session["score"], message=session.get("message"))

if __name__ == "__main__":
    app.run(debug=True)
