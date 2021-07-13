# import required libraries
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# use your email id here
username = "jackrayn99@gmail.com"

# use your App Password you
# generated above here.
password = "test@1234"

# creata a imap object
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# login
result = imap.login(username, password)

# Use "[Gmail]/Sent Mails" for fetching
# mails from Sent Mails.
imap.select('"[Gmail]/All Mail"',
readonly = True)

response, messages = imap.search(None,
            'UnSeen')
messages = messages[0].split()

# take it from last
latest = int(messages[-1])

# take it from start
oldest = int(messages[0])

for i in range(latest, latest-20, -1):
    # fetch
    res, msg = imap.fetch(str(i), "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # print required information
            print(msg["Subject"])

    if msg.is_multipart():
        # iterate over email parts
        for part in msg.walk():
            # extract content type of email
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            try:
                # get the email body
                body = part.get_payload(decode=True).decode()
                #print("Body: ********", body)
                #print(body) 

            except:
                pass
