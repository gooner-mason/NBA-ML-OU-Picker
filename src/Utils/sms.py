import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import date
from PIL import Image

def send_email_with_attachment(to_email, subject, body, attachment_path):
    # AWS SES configuration
    aws_region = 'your_aws_region'
    aws_access_key_id = 'your_aws_access_key_id'
    aws_secret_access_key = 'your_aws_secret_access_key'

    # Create an SES client
    ses_client = boto3.client('ses', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'your_verified_email@example.com'  # Replace with your verified SES email address
    msg['To'] = to_email

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PNG image
    with open(attachment_path, 'rb') as img_file:
        img_data = img_file.read()
        image = MIMEApplication(img_data, name=f"attachment_{date.today()}.png")
        msg.attach(image)

    # Send the email
    response = ses_client.send_raw_email(
        Source=msg['From'],
        Destinations=[msg['To']],
        RawMessage={'Data': msg.as_string()}
    )

    print("Email sent! Message ID:", response['MessageId'])

# Example usage
to_email = 'recipient@example.com'
subject = 'Test Email with PNG Attachment'
body = 'This is a test email with a PNG attachment.'
attachment_path = 'path/to/your/image.png'  # Replace with the path to your PNG image file

send_email_with_attachment(to_email, subject, body, attachment_path)