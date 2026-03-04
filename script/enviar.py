import smtplib
import csv
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ler credenciais de variáveis de ambiente
fromaddr = os.environ.get('EMAIL')
senha = os.environ.get('SENHA')

if not fromaddr or not senha:
    logging.error("Variáveis de ambiente EMAIL e SENHA não configuradas!")
    logging.info("Configure com: set EMAIL=seu_email / set SENHA=sua_senha (Windows)")
    logging.info("Ou crie um ficheiro .env e use python-dotenv")
    exit(1)

# Configurações
filename = "Certificado"
minicurso = "Minicurso de Robótica"
csv_path = os.path.join(os.path.dirname(__file__), 'participantes.csv')
pdf_dir = os.path.expanduser('~\\Downloads\\Participantes\\' + minicurso)

# Ler participantes do CSV
participantes = []
try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            participantes.append({'nome': row['nome'], 'email': row['email']})
    logging.info(f"{len(participantes)} participantes carregados do CSV")
except FileNotFoundError:
    logging.error(f"Ficheiro CSV não encontrado: {csv_path}")
    exit(1)

# Conectar ao SMTP
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, senha)
    logging.info("Conectado ao servidor SMTP com sucesso")
except Exception as e:
    logging.error(f"Erro ao conectar ao SMTP: {e}")
    exit(1)

# Enviar emails
enviados = 0
erros = 0

for p in participantes:
    nome = p['nome']
    toaddr = p['email']
    patharq = os.path.join(pdf_dir, nome + '.pdf')

    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = f"Certificado SEMAC XXXII - {minicurso}"

        body = (
            f"Olá, {nome}!\n"
            f"Segue seu certificado do {minicurso}.\n"
            f"Por favor, qualquer tipo de problema, favor responder esse email!\n"
            f"Obrigado por tudo e esperamos você na SEMAC XXXIII!\n\n"
            f"At.te\n"
            f"Miguel Donizeti da Silva e Silva\n"
            f"Presidente da SEMAC XXXII"
        )
        msg.attach(MIMEText(body, 'plain'))

        with open(patharq, "rb") as attachment:
            p_attach = MIMEBase('application', 'octet-stream')
            p_attach.set_payload(attachment.read())
            p_attach.add_header('Content-Disposition', f"attachment; filename={filename}.pdf")
            encoders.encode_base64(p_attach)
            msg.attach(p_attach)

        s.sendmail(fromaddr, toaddr, msg.as_string())
        logging.info(f"✅ Enviado para {nome} ({toaddr})")
        enviados += 1

    except FileNotFoundError:
        logging.warning(f"⚠️ PDF não encontrado para {nome}: {patharq}")
        erros += 1
    except Exception as e:
        logging.error(f"❌ Erro ao enviar para {nome} ({toaddr}): {e}")
        erros += 1

s.quit()
logging.info(f"\nResumo: {enviados} enviados, {erros} erros de {len(participantes)} total")
