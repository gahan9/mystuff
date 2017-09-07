import smtplib
from email.mime.text import MIMEText

def send_email(to=['example@example.com'], f_host='example.example.com', f_port=587, f_user='example@example.com', f_passwd='example-pass', subject='default subject', message='content message'):
    smtpserver = smtplib.SMTP(f_host, f_port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(f_user, f_passwd) # from email credential
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'My custom Subject'
    msg['From'] = "Admin"
    msg['To'] = ','.join(to)
    for t in to:
        smtpserver.sendmail(f_user, t, msg.as_string())
        smtpserver.close()
    print('Mail is sent successfully!!')


cont = """\
   <html>
     <head></head>
     <body>
       <p>Hi!<br>
          How are you?<br>
          Here is the <a href="http://www.google.com">link</a> you wanted.
       </p>
     </body>
   </html>
   """
try:
    send_email(message=cont)
except:
    print('Mail could not be sent')