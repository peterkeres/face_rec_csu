from lock import Lock
from Emailer import gmailMailer
import time

print("hello");

time.sleep(3)
testlock = Lock(18)
testlock.debug()
'''
testlock.unlock()

gmail = gmailMailer()
gmail.sendAlert("test.jpeg")

time.sleep(3)
'''
print('end')