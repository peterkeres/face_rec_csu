'''

'''

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


'''

'''
class gmailMailer:
    
    #variables
    fromAdd = ""
    password = ""
    toAdd = ""
    ccAdd = ""
    bccAdd = ""
    server = None
    context = None
    
    '''

    '''
    def __init__(self,fromAdd = "facescan.csu@gmail.com", password = "cpsc5155"):
        self.fromAdd = fromAdd
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        #todo: add some type of encyrption to the email
        self.context = ssl.create_default_context()
        self.toAdd = "keres_peter+secAdmin@columbusstate.edu"
        self.ccAdd = ("keres_peter+secManager1@columbusstate.edu, keres_peter+secManager2@columbusstate.edu"
                    ",keres_peter+secJames@columbusstate.edu,keres_peter+secLinda@columbusstate.edu")
        
        
    '''

    '''
    def sendAlert(self, picture):
        title = 'Alert!!! attemp of door'
        body = 'someone has tried to enter the door. Please check'
        
        self.__sendMessage(self.toAdd, title, body, picture, self.ccAdd)
        
        
    '''
    
    '''
    def __setConnection(self):
        self.server.starttls(context=self.context)
        self.server.login(self.fromAdd, self.password)
        
        
    '''

    '''
    def __cutConnection(self):
        self.server.quit()
        
 
    '''

    '''
    def __createMessage(self, toAdd, subject, message,picture = None, ccAdd = None):
        msg = MIMEMultipart()
        msg['From'] = self.fromAdd
        msg['To'] = toAdd
        if ccAdd != None: msg['Cc'] = ccAdd
        
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        if picture != None:
            imgData = open(picture, 'rb').read()
            image = MIMEImage(imgData, name=os.path.basename(picture))
            msg.attach(image)
        
        return msg
        
    '''

    '''
    def __sendMessage(self, toAdd, subject, message, picture, ccAdd = None):
        self.__setConnection()
        email = self.__createMessage(toAdd, subject, message,picture, ccAdd)
        address = toAdd.split(",") + ccAdd.split(",")
        self.server.sendmail(self.fromAdd, address, email.as_string())
        self.__cutConnection()

