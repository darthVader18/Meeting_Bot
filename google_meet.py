from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import webbrowser
import imaplib
import email
from email.header import decode_header              
import re
import schedule
from datetime import datetime


def get_email():
    # account credentials
    username = "jackrayn99@gmail.com"
    password = "test@1234"

    # create an IMAP4 class with SSL, use your email provider's IMAP server
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    # authenticate
    imap.login(username, password)

    # Use "[Gmail]/Sent Mails" for fetching
    # mails from Sent Mails.
    imap.select('"[Gmail]/All Mail"',
    readonly = True)

    response, messages = imap.search(None,
                'UnSeen')
    messages = messages[0].split()

    # for i (int(messages[i]), int(messages[i+20]), +1):
    #     i
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
                subject = msg["Subject"]
                print(subject)
                return msg


def get_subject():
    msg = get_email()
    subject = msg["Subject"]
    #print(subject)
    return subject  
    


def get_body():
    msg = get_email()
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
                return body

            except:
                pass


def get_glink():
    body = get_body()
    regex_link = ("((http|https)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)")
    link = re.findall(regex_link, body)
    g_meet = "https://meet.google.com" + link[0][-1]
    #print(g_meet)
    return g_meet


def get_time():
    subject = str(get_subject())
    #print(subject)
    joining_time = re.search(r'[0-9]{1,2}:?([0-9]{1,2})?(pm|am|AM|PM)', subject).group()
    #print(joining_time)
    if ":" not in joining_time:
        joining_time = joining_time[:-2]+":00"+joining_time[-2:]
    joining = datetime.strptime(joining_time, "%I:%M%p")
    print(joining.time())
    return str(joining.time())
    


def join_meeting(meeting_link):
    webbrowser.open(g_meet, new=1)
    time.sleep(5)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)	
    time.sleep(1)	
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(1)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(1)
    return schedule.CancelJob
    

joining_time = get_time()
g_meet = get_glink()
schedule.every().day.at(joining_time).do(join_meeting, meeting_link = g_meet)
while True:
    schedule.run_pending()
    time.sleep(1)

