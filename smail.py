import smtplib

import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail = ['smtp.gmail.com', 587]

outlook = ['smtp.live.com', 587]

office365 = ['smtp.office365.com', 587]

yahoo = ['smtp.mail.yahoo.com', 465]
yahoo_plus = ['plus.smtp.yahoo.com', 465]
yahoo_uk = ['smtp.yahoo.co.uk', 465]
yahoo_deutschland = ['smtp.mail.yahoo.com', 465]
yahoo_au = ['smtp.mail.yahoo.com.au', 465]
yahoo_nz = ['smtp.mail.yahoo.com.au', 465]

aol = ['smtp.aoi.com', 587]

types = '''gmail
outlook
office365
yahoo
yahoo+
yahoo-uk
yahoo-deutschland
yahoo-au
yahoo-nz'''

def startGmail(type):
    
def types():
    global types
    toReturn = 'GMAIL TYPES: \n' + types
    return(toReturn)
def send()
