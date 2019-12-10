#IMPORTS
import smtplib
import email
##IMPORTS FROM EMAIL
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#EXCEPTIONS
class UnknownType(Exception):
    pass
class ConnectionError(Exception):
    pass

#DEFINE SMTP MAIL TYPES
gmail = ['smtp.gmail.com', 587]
outlook = ['smtp.live.com', 587]
office365 = ['smtp.office365.com', 587]
yahoo = ['smtp.mail.yahoo.com', 465]
aol = ['smtp.aoi.com', 587]
##YAHOO SUBTYPES
yahoo_plus = ['plus.smtp.yahoo.com', 465]
yahoo_uk = ['smtp.yahoo.co.uk', 465]
yahoo_deutschland = ['smtp.mail.yahoo.com', 465]
yahoo_au = ['smtp.mail.yahoo.com.au', 465]
yahoo_nz = ['smtp.mail.yahoo.com.au', 465]
##TYPE LIST
types = '''mailtype [id]

gmail [0]
outlook [1]
office365 [2]
aol [3]
yahoo [4]
yahoo+ [4a]
yahoo-uk [4b]
yahoo-deutschland [4c]
yahoo-au [4d]
yahoo-nz [4e]'''

#MAIN
def startMail(type):
    type = type.lower()
    if type == '0':
        site = gmail[0]
        port = gmail[1]
    elif type == '1':
        site = outlook[0]
        port = outlook[1]
    elif type == '2':
        site = office365[0]
        port = office365[1]
    elif type == '3':
        site = 
        port = 
    elif type == '3a':
        site = 
        port = 
    elif type == '3b':
        site = 
        port = 
    elif type == '3c':
        site = 
        port = 
    elif type == '3d':
        site = 
        port = 
    elif type == '3e':
        site = 
        port = 
    else:
        error_ = 'UNKNOWN TYPE [ ' + type + ' ]. TRY RUNNING [ types() ]'
        raise UnknownType(error_)
    smtpServer = smtplib.SMTP()
def types():
    global types
    toReturn = 'GMAIL TYPES:\n' + types
    return(toReturn)
def send()
