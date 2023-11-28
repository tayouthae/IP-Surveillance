import pyautogui

# Take screenshot
pic = pyautogui.screenshot()

# Save the image
pic.save('screenshot.jpg')
    
    
from requests import get

ip = get('https://api.ipify.org').text
body='Public IP address is:'+ str(ip)
print (body)

import cv2
cap = cv2.VideoCapture(0)
if (cap.isOpened()):
    s, img = cap.read()
    cv2.imwrite(r"filename.jpg", img)
    cap.release()
        
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
    
    
email_send = input("Enter Email Address: ")
email_user = 'dwitpythonproject@gmail.com'
email_password = ''

subject = 'IP Address'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

    
msg.attach(MIMEText(body, 'plain'))

filename = 'filename.jpg'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)

filename2 = 'screenshot.jpg'
attachment2 = open(filename2, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment2).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename2)
msg.attach(part)

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)
server.quit()       

exit()