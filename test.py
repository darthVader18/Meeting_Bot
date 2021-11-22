# import required libraries
import imaplib
import email
from email.header import decode_header
import threading

def get_email():
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

    for i in range(oldest, latest, +1):
        # fetch
        res, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                return msg
                #print(msg)
                # print required information
                #print(msg["Subject"])

msg = []
for i in range(0,2):
    msg.append(threading.Thread(target=get_email))

for t in msg:
    t.start()
