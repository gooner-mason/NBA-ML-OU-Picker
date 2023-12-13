import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

# Access the variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_KEY")

def send_email_with_attachment(subject, body):
    # Create an SES client
    ses_client = boto3.client('ses', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


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