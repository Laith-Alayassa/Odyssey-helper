from pprint import pprint
import smtplib 
from email.message import EmailMessage
from email_info import email_id, password, test_send_to
import ssl

from plumber import write_emails


EmailAdd = email_id #senders Gmail id over here
Pass = password #senders Gmail's Password over here 

late_students = write_emails()
pprint(late_students)
for student, info in late_students.items():
    msg = EmailMessage()
    msg['Subject'] = '[Action Required]Late Item Notice' # Subject of Email
    msg['From'] = EmailAdd
    msg['To'] = test_send_to
    body = info[-1]
    
    msg.set_content(body) # Email body or Content

    context = ssl.create_default_context()


    #### >> Code from here will send the message << ####
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
        smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
        smtp.send_message(msg) #This Sends the message
