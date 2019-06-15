# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import sys

import json

with open(sys.argv[1]) as file:
	secrets = json.loads(file.read())
	print(secrets["ACCOUNT SID"])


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


account_sid = secrets["ACCOUNT SID"]
auth_token = secrets['AUTH TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Kristen has a great butt holy shit",
                     from_='+16506703575',
                     to='+16507937076'
                 )

print(message.sid)