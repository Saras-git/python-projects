from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        low = int(request.form["low"])
        high = int(request.form["high"])
        difficulty = request.form["difficulty"]

        if difficulty == "easy":
            chances = 10
        elif difficulty == "medium":
            chances = 7
        else:
            chances = 5

        number = random.randint(low,high)

        session["number"] = number
        session["low"] = low
        session["high"] = high
        session["chances"] = chances
        session["attempt"] = 0

        return redirect(url_for("game"))

    return render_template("index.html")


@app.route("/game", methods=["GET","POST"])
def game():

    message = ""
    number = session.get("number")
    chances = session.get("chances")
    attempt = session.get("attempt")

    if request.method == "POST":

        guess = int(request.form["guess"])
        attempt += 1
        session["attempt"] = attempt

        if guess == number:
            message = f"🎉 Correct! You guessed the number in {attempt} attempts!"
            session.clear()

        elif attempt >= chances:
            message = f"❌ Game Over! The number was {number}"
            session.clear()

        elif guess > number:
            message = "📉 Too High! Try Lower"

        else:
            message = "📈 Too Low! Try Higher"

    return render_template(
        "game.html",
        message=message,
        chances=session.get("chances"),
        attempt=session.get("attempt"),
        low=session.get("low"),
        high=session.get("high")
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
