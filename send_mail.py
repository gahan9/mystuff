import smtplib
def send_email(to='admin@example.com', f_host='send.one.com', f_port=587, f_user='example@example.com', f_passwd='example_pass', subject='cEyes-Registration', message='content message'):
    smtpserver = smtplib.SMTP(f_host, f_port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(f_user, f_passwd) # from email credential
    header = 'To:' + to + '\n' + 'From: ' + f_user + '\n' + 'Subject:' + subject + '\n'
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
    message = header + '\n' + cont + '\n\n'

    smtpserver.sendmail(f_user, to, message)
    smtpserver.close()
    print('Mail is sent successfully!!')