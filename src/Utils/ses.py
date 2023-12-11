import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import date
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

# Access the variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_KEY")

def send_email_with_attachment(body, attachment_path=None):
    # Create an SES client
    ses_client = boto3.client('ses', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = "Jar's Picks"
    msg['From'] = 'masonjmaier@gmail.com' # Replace with your verified SES email address
    msg['To'] = 'masonjmaier@gmail.com'

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PNG image
    if attachment_path: 
        with open(attachment_path, 'rb') as img_file:
            img_data = img_file.read()
            image = MIMEApplication(img_data, name=f"jars_picks_{date.today()}.png")
            msg.attach(image)

    # Send the email
    response = ses_client.send_raw_email(
        Source=msg['From'],
        Destinations=[msg['To']],
        RawMessage={'Data': msg.as_string()}
    )

    print("Email sent! Message ID:", response['MessageId'])