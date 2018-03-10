import twilio
from twilio.rest import Client

print(twilio.__version__)

# put your own credentials here
account_sid = "AC9e9f1de884cd9ee32a2dc04f04e6557b"
auth_token = "db3469a5d5fef0d4c121f1d4437c9ec4"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+27765306596",
    from_="+27875504622",
    body="This is the ship that made the Kessel Run in fourteen parsecs?"
)