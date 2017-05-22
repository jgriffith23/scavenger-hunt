"""Functions that connect to Twilio, send clues, and receive user answers."""

from twilio.rest import Client
import os

TWILIO_PHONE = os.environ.get("TWILIO_PHONE")

def get_client():
    """Connect to Twilio and instantiate a client."""

    twilio_acct_sid = os.environ.get("TWILIO_ACCT_ID")
    twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    return Client(twilio_acct_sid, twilio_auth_token)

    
def send_clue(player):
    """Send a scavenger hunt player a clue via SMS."""
    
    client = get_client()

    # TODO: Eventually, this will come from a database...
    clue = "What do you get when you cross an elephant and a rhino?"

    message = client.api.account.messages.create(
        to=player,
        from_=TWILIO_PHONE,
        body=clue,
    )

