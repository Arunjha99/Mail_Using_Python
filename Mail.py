import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

senderAddr = "Sender's Email Address"
receiverAddr = "Receiver's Email Address"

msg = MIMEMultipart()

msg['From'] = senderAddr
msg['To'] = receiverAddr
msg['Subject'] = "Your Subject"
body = "Your Message"

msg.attach(MIMEText(body, 'plain'))
filename = "test.txt"
attachment = open("D:\\Python\\test.txt", "r+")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment: filename= %s" % filename)
msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(senderAddr, "Sender's Gmail Password")
text = msg.as_string()
s.sendmail(senderAddr, receiverAddr, text)
s.quit()

