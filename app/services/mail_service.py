import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings


def send_activation_email(to_email: str, OPT_code: str):
    
    receiver_email = to_email
    sender_email = settings.SENDER_EMAIL    
    sender_password = settings.SENDER_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "Chào mừng bạn đến với ứng dụng của chúng tôi!"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """
    <html>
    <body>
        <h1>Xin chào!</h1>
        <p>Cảm ơn bạn đã đăng ký ứng dụng của chúng tôi.</p>
        <p>Mã OTP của bạn là: <strong>{}</strong></p>
        <p>Vui lòng sử dụng mã này để xác minh tài khoản của bạn.</p>
    </body>
    </html>
    """.format(OPT_code)

    mime_text = MIMEText(html, "html")
    message.attach(mime_text)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        return False