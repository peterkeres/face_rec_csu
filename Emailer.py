

import smtplib

'''
fill out info
'''
fromadd = "facescan.csu@gmail.com"
toadd = "keres_peter@columbusstate.edu"
password = "cpsc5155"

'''
sets up connection to send an email off
'''
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromadd, password)

'''
the messaage
'''
msg = "If you are reading this, i got it too send an email! one step closer."

'''
sends off the email
'''
server.sendmail(fromadd, toadd, msg)

'''
cuts connection to the server.
'''
server.quit()



