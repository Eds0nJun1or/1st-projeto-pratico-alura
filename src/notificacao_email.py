import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo_mensagem): # Configurações do servidor SMTP
    smtp_host = 'smtp.example.com'
    smtp_porta = 587
    email_rem = 'seu_email@example.com'
    senha = 'sua_senha'

## Configurar mensagem
mensagem = MIMEMultipart()
mensagem['From'] = email_rem
mensagem['To'] = destinatario
mensagem['Subject'] = assunto
mensagem.attach(MIMEText(corpo_mensagem, 'plain'))

## Conectar ao servidor SMTP e enviar e-mail
server = smtplib.SMTP(smtp_host, smtp_porta)
server.starttls()
server.login(email_rem, senha)
server.sendmail(email_rem, destinatario, mensagem.as_string())
server.quit()

### Exemplos de como usar:

destinatario = 'destinatario@example.com'
assunto = 'Alerta: Falha no sistema!'
corpo_mensagem = 'O sistema encontrou uma falha crítica. Por favor, verifique imediatamente.'
enviar_email(destinatario, assunto, corpo_mensagem)