import csv
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(from_email, password, to_email, body, attachments=[]):
    #Creating message object
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] =  to_email
    message['Subject'] = "Join the fight to keep Compost in NYC"
    message.attach(MIMEText(body, 'html'))
    
    for attachment in attachments:
        # Create a MIME part for each file
        part = MIMEBase('application', 'octet-stream')
        try:
            with open(attachment, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)  # Encode the attachment in base64
            part.add_header('Content-Disposition', f'attachment; filename="{attachment.split("/")[-1]}"')
            message.attach(part)
        except Exception as e:
            print(f"Could not attach file {attachment}. Error: {e}")
            continue
    
    
    try:
        #logining into the email and sending the message
        # Could be optimized by sending making a function that sends the email and once logged in, loop through it and send. This current setup, I log in everytime making the code run slower
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
        
        
# Index's serve as a key for every entry

Status = []  # Wether the email has been sent or not
Amount = [] # Amount of compost each recivier has obtained from us
Date = [] # Date we last worked with them
Contact = [] # The contact from CSV, some numbers and/or email
Email = [] # List only for emails
attachments = [ # The attachments added to the email being sent
    'attachment_1.jpg',
    'attachment_2.jpg',
    'attachment_3.pdf',
    'attachment_4.pdf',
    'attachment_5.pdf'
]


from_email = '______@gmail.com' # Enter gmail name here
password = '_____' # Enter passcode from google project here
host = "smtp.gmail.com"
port = 465

# Obtaining the data from the CSV file and adding it to respective lists
with open('PartnerForCompost.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    
    for coulmn in reader:
        Status.append(coulmn[0])
        Amount.append(coulmn[1])
        Date.append(coulmn[2])
        Contact.append(coulmn[3])

# Regex to only extract emails from the data the contact list
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

for entries in Contact:
    found_emails =  email_pattern.findall(entries)
    Email.append(found_emails)
    
# HTML message that the recivers will see
HTML_Template = """
<html>
 <body>
       # Enter html for the emaiil here
 </body>
</html>
"""
# Counter will serve as the index
# For loop that calls the send email function
counter = 0
for emails in testEmails: ## for production its Email instead
    fortmatted_html_body = HTML_Template.format(amount=Amount[counter], date=Date[counter]) # Personalizing emails to the entry
    counter = counter + 1
    send_email(from_email, password, emails, fortmatted_html_body, attachments)
