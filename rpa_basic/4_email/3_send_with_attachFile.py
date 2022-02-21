import smtplib
from account import*
from email.message import EmailMessage


msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다 "#제목 적기 
msg["From"] =EMAIL_ADDRESS   #보내는사람
msg["To"]="hp980724@gmail.com" #받는 사람 
msg.set_content("다운 받으세요")

# MIME TYPE

# msg.add_attachment()

#이미지
with open("btn_text.png","rb") as f:
    msg.add_attachment(f.read(),maintype="image",subtype="png",filename=f.name)

# pdf
with open("test.pdf","rb") as f:
    msg.add_attachment(f.read(),maintype="application",subtype="pdf",filename=f.name)


# excel
with open("test.xlsx","rb") as f:
    msg.add_attachment(f.read(),maintype="application",subtype="octet-stream",filename=f.name)


with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)