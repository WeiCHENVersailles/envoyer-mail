import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#MESSAGEMAIL = 'Envoyer un mail lorsqu\'une page web est défaillante Les admins système utilisent souvent des alertes SMS ou des alertes mail pour être averti en cas de soucis sur leur serveur. Prenons un cas pratique où nous sommes dans la situation d\'un serveur qui surveille un autre. Le premier check toutes les minutes si le deuxième serveur répond pour une requête HTTP et surtout si son temps de réponse est acceptable:'

def envoyer_mail(subject_mail,message_mail):
  msg = MIMEMultipart()
  msg['From'] = 'guiguiprofpython@gmail.com'
  msg['To'] = 'chenwei822@gmail.com'
  msg['Subject'] = subject_mail 
  message = message_mail
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP('smtp.gmail.com', 587)
  mailserver.ehlo()
  mailserver.starttls()
  mailserver.ehlo()
  mailserver.login('guiguiprofpython@gmail.com', 'Guiguidu94')
  mailserver.sendmail('chenwei822@gmail.com', 'chenwei822@gmail.com', msg.as_string())
  mailserver.quit()

#def main():
  #envoyer_mail('Salut! Guigui', MESSAGEMAIL)

#main()