from audioop import reverse
from imap_tools import MailBox
from account import *

# mailbox=MailBox("imap.gmail.com",993)
# mailbox.login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder="INBOX")

with MailBox("imap.gmail.com",993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    # 전체 메일 가져오기 
    # for msg in mailbox.fetch(limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # # 읽지 않은 메일가져오기
    # for msg in mailbox.fetch('(UNSEEN)',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 특정인이 보낸 메일 가져오기 
    # for msg in mailbox.fetch('(FROM hp980724@gmail.com)',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 어떤 글자를 포함하는 메일 (제목,본문 )
    # 작은 따옴표로 먼저 감싸고 , 실제 TEXT 부분은 큰 따옴표로 감싸준다. 
    # for msg in mailbox.fetch('(TEXT "test")',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 어떤 글자를 포함하는 메일 (제목만 )
    # for msg in mailbox.fetch('(SUBJECT "test mail")',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 한글은 하기 힘들다 따라서 야매로 하기 
    # for msg in mailbox.fetch(limit=5,reverse=True):
    #     if "테스트" in msg.subject:
    #         print("{} {}".format(msg.from_,msg.subject))

    # 특정 날짜 이후의 메일 
    # for msg in mailbox.fetch('(SENTSINCE 08-Nov-2021)',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    
    # 특정 날짜의 메일 
    # for msg in mailbox.fetch('(ON 08-Nov-2021)',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    #2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(SENTSINCE 08-Nov-2021 SUBJECT "test mail")',limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 2중에 하나라도 만족하는 메일 (또는 주건 
    for msg in mailbox.fetch('(OR SENTSINCE 08-Nov-2021 SUBJECT "test mail")',limit=5,reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))