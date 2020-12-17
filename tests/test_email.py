'''
a Test that will send off a email alert
'''

from email_mod.Emailer import gmailMailer
import time

print("hello, testing out the email mod for gmail");

gmail = gmailMailer()
gmail.sendAlert("test_email.jpeg")

print('email sent')

time.sleep(3)

print('end')