import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Ayo Osota'
email['to'] = 'orimadegunadebanjo@gmail.com'
email['subject'] = 'You won $1,000,000 dollars'


email.set_content(html.substitute(name='Adebanjo'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('osotaayomikun@gmail.com', 'lqlb mzqq zyle mvlc')
    smtp.send_message(email)
    print('all good')
