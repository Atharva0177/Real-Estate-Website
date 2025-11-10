from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='mandavkaratharva@gmail.com',
    MAIL_PASSWORD='crmj obti iwsr zkvt'
)

mail = Mail(app)

with app.app_context():
    msg = Message(
        subject="Test Email from Flask",
        sender=app.config['MAIL_USERNAME'],
        recipients=["mandavkaratharva4@gmail.com"],
        body="This is a test email sent using Flask-Mail and Gmail App Password."
    )
    mail.send(msg)
    print("✅ Email sent successfully!")
