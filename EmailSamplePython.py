import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "nickftestaccount@yahoo.com"
toaddr = "nickftestaccount@yahoo.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"

varInput1 = raw_input("Tell me something nice:")
varInput2 = raw_input("Tell me something naughty:")
varInput3 = raw_input("Say goodbye in a language of your choice")

body = varInput1 + " " + varInput2 + " " + varInput3
msg.attach(MIMEText(body,'plain'))

print "Created Message"

server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

print "Trying to Connect"
server.starttls()
print "Connected"
server.login(fromaddr,"****") #REMOVE THIS BEFORE SUBMITTING
print "Logged In"
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print "Sent Message"
server.quit()

