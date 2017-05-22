from flask import Flask, request
import messages

app = Flask(__name__)

@app.route("/")
def display_start():
    """Show form where player can enter phone number to start the game."""


@app.route("/", methods=["POST"])
def start_game():
    """Process form to begin scavenger hunt."""

    player_phone = request.form.get("phone")

    if player_phone:
        messages.send_clue(player, first_clue)

@app.route("/clue")
def send_clue():
    for item in request.form.items():
        print item

    player = request.form.get("From")

    if player is not None:
        sms_text = request.form.get("Body")
        messages.send_clue(player)

    return "Send a text to get a clue, dude!"

@app.route("/test")
def test():
    return "We all live in a yellow submarine..."

if __name__ == "__main__":
    app.run(debug=True)
