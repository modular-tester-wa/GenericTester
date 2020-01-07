import smtplib
import mimetypes

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def SendFile(filen):
    #Details
    addr_to = "AMarquez@westernautomation.com" #destination Email
    addr_from = ""#Source Email

    # Create Multipart object
    msg = MIMEMultipart()
    msg['From']=addr_from
    msg['To']=addr_to
    msg['Subject']="it has an attached file"

    # Attach a file
    file = open(filen, "rb")
    attach_file = MIMEBase('multipart', 'encrypted')
    attach_file.set_payload(file.read())
    file.close()

    encoders.encode_base64(attach_file)
    attach_file.add_header('Content-Disposition', 'attachment', filename=filen)
    msg.attach(attach_file)

    # Login
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(addr_from,'') #Add password among''

    # Send
    mailServer.sendmail(addr_from, addr_to, msg.as_string())

    # stmp close
    mailServer.close()
