import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_with_attachment(subject, body):
    # Create an SES client
    ses_client = boto3.client('ses')

    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'masonjmaier@gmail.com' 
    msg['To'] = 'masonjmaier@gmail.com'

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))


    # Send the email
    response = ses_client.send_raw_email(
        Source=msg['From'],
        Destinations=[msg['To']],
        RawMessage={'Data': msg.as_string()}
    )

    print("Email sent! Message ID:", response['MessageId'])