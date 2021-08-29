  
import os
from twilio.rest import Client



account_sid = os.environ['ACaa77ea155c8f85c61940555a67ab9744']
auth_token = os.environ['90951b1fdb81e6dbd9b73ae37ff10586']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)
