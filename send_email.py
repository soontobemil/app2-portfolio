import smtplib
import ssl
import certifi
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "krjayvancouver@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "krjayvancouver@gmail.com"
    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
