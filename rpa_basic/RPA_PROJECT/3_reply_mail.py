import smtplib
from imap_tools import MailBox
from smtplib import *
from email.message import EmailMessage
from account import *

max_value =3 # 최대 선정자 수 
applicant_list = [] # 지원자 리스트 

print("[1. 지원자 메일 조회]")

with MailBox("imap.gmail.com",993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    index = 1 #순번 
    for msg in mailbox.fetch('(SENTSINCE 20-Feb-2022)'): # 2022년 2월20일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname,phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임: {} 전화번호 : {}".format(index,nickname,phone))
            applicant_list.append((msg,index,nickname,phone))
            index +=1


print("[2. 선정/ 탈락 메일 발송 ]")

#  [선정 안내 메일 ]
# 제목 : 파이썬 특강 안내
# 본문 : xx님 축하드립니다 특강 대상자로 선정 (선정 순번 1번 )

# [탈락 안내 메일 ]
# 제목: 파이썬 특강 안내 [탈락]
# 본문: xx 님 아쉽게도 탈락입니다, 취소 인원이 발생하는 경우 연락드리겠습니다(대기순번 1번)
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_

        # index = applicant[1]
        # nickname =applicant[2]
        # phone =applicant[3]
        # 위에 3문장과 같음 
        index,nickname,phone =applicant[1:]
        
        title =None
        content = None

        if index <=max_value:
            title = "파이썬 특강 안내 [선정]"
            content = "{}님 축하드립니다 특강 대상자로 선정 (선정 순번 {}번 )".format(nickname,index)
        else:
            title = "파이썬 특강 안내 [탈락]"
            content ="{} 님 아쉽게도 탈락입니다, 취소 인원이 발생하는 경우 연락드리겠습니다(대기순번 {}번)".format(nickname,index-max_value)

        msg =EmailMessage()
        msg["Subject"]=title
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname,"님에게 메일 발송 완료 ")
