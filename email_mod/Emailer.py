'''
Peter keres
Nov 4 2019
v1.0

This file handles sending any email notication that the 'facial scanning' app needs

Each class in this file will handle sending emils for its own service. Currently,
there is only the 'Gmail' service developed. If you wanted to use another service, you would
make a seperate class for that.

Each class only has one public outfaceing method, that is the 'sendAlert()' method.
send this method the path to the picture to be sent and it will send to system admins. 

currently, the list of system admins are hard coded into the class. This will be made into
a method at a later date.

Also the password to the email server i am using is also hardcoded. Please be cool and dont
hold this account for ransom. 

'''

#libarys needed 
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


'''
This class handles sending emails though a Gmail service 
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
    Sets up defalut variables to be used by this class. Also sets up a list of system admin emails
    
    @pram
        fromAdd: what email address is being used to send off the emails
        password: the password neededt to access the fromAdd email account
    '''
    def __init__(self,fromAdd = "facescan.csu@gmail.com", password = "cpsc5155"):
        self.fromAdd = fromAdd
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        #encyrption to the email
        self.context = ssl.create_default_context()
        self.toAdd = "keres_peter+secAdmin@columbusstate.edu"
        self.ccAdd = ("keres_peter+secManager1@columbusstate.edu, keres_peter+secManager2@columbusstate.edu"
                    ",keres_peter+secJames@columbusstate.edu,keres_peter+secLinda@columbusstate.edu, heycassidy@gmail.com")
        
        
    '''
    this sends off an alert message to all system admins with an attached picture
    @PRAM
        picture: the path to the picture needing to be sent
    '''
    def sendAlert(self, picture):
        title = 'Alert!!! attemp of door'
        body = 'someone has tried to enter the door. Please check'
        
        self.__sendMessage(self.toAdd, title, body, picture, self.ccAdd, self.bccAdd)
        
        
    '''
    this sets the connection to the Gmail email server
    '''
    def __setConnection(self):
        self.server.starttls(context=self.context)
        self.server.login(self.fromAdd, self.password)
        
        
    '''
    This cuts the connection to the Gmail emai server
    '''
    def __cutConnection(self):
        self.server.quit()
        
 
    '''
    this creates the Email object to be sent
    @PRAM
        toAdd: who you are sending this too
        subject: title of the email
        message: the message of the email
        picutre: any attaced picture
        ccAdd: list of other address you want to send too
    @RETURN
        the email object
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
    this will handle setting the conection, creating the email object, sending the email, and
    cutting the email object.
    @PRAM:
        toAdd: who you are sending it too
        subject: title of email
        message: message of the email
        picture: any attaced picture
        ccAdd: any addresses you want as CC
        bccAdd: any address you want as BCC
    '''
    def __sendMessage(self, toAdd, subject, message, picture, ccAdd = None, bccAdd = None):
        self.__setConnection()
        email = self.__createMessage(toAdd, subject, message,picture, ccAdd)
        address = toAdd.split(",") + ccAdd.split(",") + bccAdd.split(",")
        self.server.sendmail(self.fromAdd, address, email.as_string())
        self.__cutConnection()

