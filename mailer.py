import smtplib
import os
from email.message import EmailMessage


def send_email(subject, body, attachment_path):

    EMAIL_USER = os.environ.get("EMAIL_USER")
    EMAIL_PASS = os.environ.get("EMAIL_PASS")

    if not EMAIL_USER or not EMAIL_PASS:
        print("Variabili EMAIL_USER o EMAIL_PASS mancanti.")
        return

    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER
    msg["Subject"] = subject

    msg.set_content(body)

    # Allegato PDF
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Email inviata correttamente.")
    except Exception as e:
        print("Errore invio email:", e)
