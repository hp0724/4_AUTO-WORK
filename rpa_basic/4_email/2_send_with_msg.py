import smtplib
from account import*
from email.message import EmailMessage


msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다 "#제목 적기 
msg["From"] =EMAIL_ADDRESS   #보내는사람
msg["To"]="hp980724@gmail.com" #받는 사람 

# # 여러 명에게 메일을 보낼 때 
# msg["To"]="hp980724@gmail.com,hp980724@gmail.com"

# # to_list =["hp980724@gmail.com","hp980724@gmail.com"]
# # msg =", ".join(to_list)

# # 참조 
# msg["Cc"] ="hp980724@gmail.com"

# # 비밀참조 
# msg["Bcc"]="hp980724@gmail.com"


msg.set_content("테스트 본문입니다") #본문 

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)