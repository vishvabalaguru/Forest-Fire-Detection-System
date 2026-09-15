import os
import time                                     
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import imghdr

def report_send_mail(label, image_path):

    with open(image_path, 'rb') as f:
        img_data = f.read()
    fromaddr = "vishva.csr122@gmail.com"
    toaddr = "vishvavishvabalaguru@gmail.com"
               
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Alert,E.G.S.Pillay Engineering College,GG BLOCK."

    body = label
    msg.attach(MIMEText(body, 'plain'))
    
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image)

      
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "ywfbiolgmllaaomp") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()

