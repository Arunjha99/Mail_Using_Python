import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

senderAddr = "aarunjha01@gmail.com"
receiverAddr = "arun.jha.cse99@gmail.com"

msg = MIMEMultipart()

msg['From'] = senderAddr
msg['To'] = receiverAddr
msg['Subject'] = "Important Notice from TPO"
body = "This is to inform you that Infosys is going to recruit 2021 batch today."

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
s.login(senderAddr, "7898_361693")
text = msg.as_string()
s.sendmail(senderAddr, receiverAddr, text)
s.quit()

