import smtplib

fromaddr = 'shane.richards212@gmail'
toaddr = 'david@alteroo.com'

message = """From: {} <{}> 
To: {} <{}>
Subject: {}

{}
"""

messagetosend = message.format(
	fromname,
	fromaddr,
	toname,
	toaddr,
	subject,
	msg)

# Credentials
username = 'shane.richards212@gmail.com'
password = 'curryishot'

# The actual message
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()