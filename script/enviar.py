import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

mail = [
"luiza.cavarcan@hotmail.com",
"priscillasfcarrossoni@gmail.com",
"daphne.pereira@unesp.br",
"murilotolentinoruf@hotmail.com",
"gabrieldalalana@hotmail.com",
"bruninhoicem@gmail.com",
"jean.achour@unesp.br",
"douglas.eduardo.2003@gmail.com",
"haru02w@protonmail.com",
"glucasemanuel@gmail.com",
"igor.y.ide@unesp.br",
"cadu35918@gmail.com",
"rafaelmello625@gmail.com",
"tadeijulia@gmail.com",
"ppcardana@hotmail.com",
"victoria.bechara@unesp.br",
"gustavo200699@hotmail.com",
"laracesquini@gmail.com",
"markingcarlos@gmail.com",
"paulo.filho@unesp.br",
"abg.takehara@gmail.com",
"ra.yu.takehara@gmail.com",
"julia.gubolin.2@gmail.com"



]
name = [
"Luiza Guimarães Cavarçan",
"Priscilla Shiota Fedichina Carrossoni",
"Daphne Lie Haranaka Pereira",
"Murilo Tolentino Rufino",
"Gabriel Jose Pellisser Dalalana",
"Bruno Cesar Silva Rodrigues",
"Jean Rayhan Vieira Achour",
"Douglas Eduardo da Silva",
"João Victor Millane",
"Lucas Emanuel Genova",
"Igor Yoshimitsu Ide",
"Carlos Eduardo Da Rocha Morais",
"Rafael de Mello",
"Julia Tadei",
"Pedro Benedicto de Melo Cardana",
"Victória Bechara",
"Gustavo Pereira Pazzini",
"Lara Cesquini Stopa",
"Carlos Alberto de Souza Junior",
"Paulo Tavares Borges Filho",
"Ana Beatriz Gomes Takehara",
"Rafael Yukio Takehara Carvalho",
"Julia Rodrigues Gubolin"

]
# mail=[
#     "silva.silva@unesp.br"
# ]
# name = [
#     "Arthur Borsonaro Uezu"
# ]
fromaddr = 'silva.silva@semac.cc'
filename = "Certificado"
minicursor = "Minicurso de Robótica"
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, '&Miguel96') 

for i in range(len(name)):
     
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['Subject'] = "Certificado SEMAC XXXII - "+minicursor
    patharq = 'C:\\Users\\migue\\Downloads\\Participantes\\'+minicursor+'\\'+name[i]+'.pdf'
    toaddr = mail[i]
    msg['To'] = toaddr
    print(toaddr)
    attachment = open(patharq,"rb") 
    body = "Olá, "+ name[i] + "!\nSegue seu certificado do "+ minicursor+".\nPor favor, qualquer tipo de problema, favor responder esse email!\nObrigado por tudo e esperamos você na SEMAC XXXIII!\n\nAt.te\nMiguel Donizeti da Silva e Silva\nPresidente da SEMAC XXXII"
    msg.attach(MIMEText(body, 'plain')) 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    p.add_header('Content-Disposition', "attachment; filename= " +filename +".pdf") 
    encoders.encode_base64(p)
    msg.attach(p) 
    text = msg.as_string() 
    #/₢print(text)/
    s.sendmail(fromaddr, toaddr, text) 
    
s.quit() 
