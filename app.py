from twilio.rest import Client
import config
cl = Client(config.account_sid, config.auth_token)
cl.messages.create(
    from_='+14246780245',
    body="PyMessenger Demo: This test SMS was sent by Lokesh using Python, Twilio REST API, and a virtual environment. Message delivery confirms successful integration and authentication.",
    to='+918008070234'
)
print("message sent !")
