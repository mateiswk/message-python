import os
from twilio.rest import Client
# get code for SMS from python helper library
sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ[TWILIO_AUTH_TOKEN]
c = Client(sid , auth_token)
message = client.messages
create(
    body='ba iti pic netul'
    from_='+40723624113'
    to='+40787836511'
)
