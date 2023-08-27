import smtplib
import ssl
import certifi

host = "smtp.gmail.com"
port = 465

username = "krjayvancouver@gmail.com"
password = ""

receiver = "krjayvancouver@gmail.com"
context = ssl.create_default_context(cafile=certifi.where())

message = """\
Subject: Hi !
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
