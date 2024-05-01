import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, "your_password")
        server.sendmail(sender_email, receiver_email, message.as_string())

def monitoring_alerts():
    # Check for anomalies and delays
    anomaly_detected = True
    if anomaly_detected:
        send_email_alert("Anomaly Detected in Ad Data Pipeline", "Anomaly detected in data processing. Please investigate.")

if __name__ == "__main__":
    monitoring_alerts()
