#IMPORT
##OS, SYS, TIME
import os
import sys
import time
##SMTPLIB
import smtplib 
##EMAIL
import email
###FROM EMAIL
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#GET OS INFO
dir_path = os.getcwd()
filespace = os.path.sep

#CREATE SMTP SESSION
s = smtplib.SMTP('smtp.gmail.com', 587) 
#ACTIVATE TLS FOR SECURITY
s.starttls() 
#GET SENDER INFO
while True:
    try:
        usr = input('ENTER SENDER EMAIL ID >')
        pw = input('ENTER SENDER PASSWORD >')
#LOGIN
        s.login(usr, pw)
        break
    except Exception as ex_:
        print ('UNKNOWN EXCEPTION AT ' + str(ex_))
        print ('LOGIN MAY BE INCORRECT, OR SERVER MAY BE BUSY')
        print ('YOU MIGHT NEED TO ALLOW LESS SECURE APPS ON THE SENDER GMAIL ACCOUNT AT\nhttps://myaccount.google.com/lesssecureapps\nYOU MAY ALSO NEED TO GO TO\nhttps://www.google.com/accounts/DisplayUnlockCaptcha')

#FUNCTIONS
def sendMessage(server, user, rec, message_, subject=''):
        message = MIMEMultipart()
        message["From"] = user
        message["To"] = rec
        message["Subject"] = subject
        message["Bcc"] = rec
        message.attach(MIMEText(message_, "plain"))
        message = message.as_string()
        try:
            server.sendmail(user, rec, message)
            return(True)
        except Exception as ex_:
            print ('UNKNOWN EXCEPTION AT ' + str(ex_))
            return(ex_)
def repeatingMessage(server, user):
    #GET MESSAGE TO SEND
    message = input('ENTER MESSAGE TO REPEAT >')
    #GET RECEIVER
    rec = input('ENTER WHO TO SEND MESSAGE TO >')
    #SEND MESSAGE
    print ('PRESS CTRL+C TO TERMINATE SESSION')
    while True:
        try:
            time.sleep(1.5)
            response = sendMessage(server, user, rec, message)
            if response != True:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            print ('ENDING SESSION')
            break
def basicMessage(server, user):
    while True:
        #GET MESSAGE TO SEND
        message = input('ENTER MESSAGE TO SEND, OR TYPE %STOP TO STOP >')
        if message.lower() == '%stop':
            break
        #GET RECEIVER
        rec = input('ENTER WHO TO SEND MESSAGE TO >')
        #SEND MESSAGE
        sendMessage(server, user, rec, message)
def subjectMessage(server, user):
    while True:
        #GET MESSAGE TO SEND
        subject = input('ENTER SUBJECT TO SEND, OR TYPE %STOP TO STOP >')
        if subject.lower() == '%stop':
            break
        #GET MESSAGE
        message = input('ENTER MESSAGE TO SEND >')
        #GET RECEIVER
        rec = input('ENTER WHO TO SEND MESSAGE TO >')
        #SEND MESSAGE
        sendMessage(server, user, rec, message, subject)

#MAIN
options = '''OPTIONS:
[e] EXIT THE PROGRAM
[b] SEND A BASIC, TEXT-ONLY MESSAGE WITHOUT SUBJECT
[r] REPEATEDLY SEND A BASIC MESSAGE, WITH A USER-SET DELAY
[s] SEND A BASIC MESSAGE WITH A SUBJECT

SELECT AN OPTION >'''
while True:
    opt = (input(options)).lower()
    if opt == 'e' or opt == '[e]':
        break
    elif opt == 'b' or opt == '[b]':
        basicMessage(s, usr)
    elif opt == 'r' or opt == '[r]':
        repeatingMessage(s, usr)
    elif opt == 's' or opt == '[s]':
        subjectMessage(s, usr)
    else:
         print ('UNKNOWN OPTION ' + opt)
#TERMINATE SESSION
s.quit()
print ('SESSION TERMINATED')

