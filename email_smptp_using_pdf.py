import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage


def attachment_file(filename, email_text, password,from_address : str,to_address : str , subject:str):
    email_content = f"""{email_text}"""
    email = MIMEMultipart()
    email['Subject'] = subject
    email['From'] = from_address
    email['To'] = to_address
    email.attach(MIMEText(email_content, 'plain'))

    if len(filename) > 1: #for 2 files or more !
        for n in filename:
            attachment_file = n.split('/')[-1]
            file_name = open(n, 'rb')
            payload = MIMEBase('application', 'octet-stream')
            payload.set_payload(file_name.read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Disposition', 'attachment', filename=attachment_file)
            email.attach(payload)
    else:
        attachment_file = filename[0].split('/')[-1]
        file_name = open(filename[0], 'rb') # if just one file !
        payload = MIMEBase('application', 'octet-stream')
        payload.set_payload(file_name.read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Disposition', 'attachment', filename=attachment_file)
        email.attach(payload)

    smptp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)

    smptp_connector.starttls()
    smptp_connector.login(from_address,password)

    text = email.as_string()
    smptp_connector.sendmail(from_address, to_address, text)
    smptp_connector.quit()
    print('Mail Sent')

def sending_without_file(email_adress:str, to_adress:str, subject:str, text:str, password):
    email = EmailMessage()

    email_content = f'''
    {text}
    '''

    email['Subject'] = f'{subject}'
    email['From'] = f'{email_adress}'
    email['To'] = f'{to_adress}'

    email.set_content(email_content)

    smptp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)

    smptp_connector.starttls()
    smptp_connector.login(email_adress,password)

    smptp_connector.send_message(email)
    print('Mail sent')
    smptp_connector.quit()
