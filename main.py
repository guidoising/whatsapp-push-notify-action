import os
from twilio.rest import Client

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Push event triggered in master branch',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['TO_WHATSAPP_NO']
                          )

print("Message ID:",message.sid)
