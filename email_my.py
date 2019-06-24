def send_email(from_addr, to_addr, password, smtp_server, server_port):

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import os

    fromaddr = from_addr
    toaddr = to_addr

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Screenshots for test case"

    # string to store the body of the mail
    body = "Test case completed!"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    dir_cont = os.listdir('.')
    for el in dir_cont:
        if el[-4:] == '.png':
            # open the file to be sent
            filename = el
            attachment = open(el, "rb")
            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')
            # To change the payload into encoded form
            p.set_payload(attachment.read())
            # encode into base64
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            # attach the instance 'p' to instance 'msg'
            msg.attach(p)
            os.remove(el)

    # creates SMTP session
    s = smtplib.SMTP(smtp_server, server_port)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
