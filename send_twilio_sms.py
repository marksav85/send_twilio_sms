from twilio.rest import Client

# Your Accound Sid and Auth Token from twilio
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="",    # insert destination number
    from_="",  # insert twilio number
    body="") # insert message

print (message.sid)
