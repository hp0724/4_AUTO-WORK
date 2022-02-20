# 파일 기본 
from msilib.schema import CheckBox
import os 
# print(os.getcwd()) # current working directory 현재 작업 공간 
# #os.chdir("RPA_BASIC") #rpa_basic 으로 작업공간이동 
# # print(os.getcwd())
# os.chdir("..") #부모 폴더로 이동 
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동 
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path= os.path.join(os.getcwd(),"my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기 
# r 은 문자 그대로 출력 탈출문자 x 
# print(os.path.dirname(r"C:\Users\hp072\Desktop\파이썬\4_AUTO WORK\rpa_basic"))


# # 파일 정보 가져오기 
# import time
# import datetime 
# # 파일의 생성 날짜 
# file_path ="2_desktop/11_file_system.py"
# ctime=os.path.getctime(file_path)
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y년:%m월:%d일 %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y년:%m월:%d일 %H:%M:%S"))

# # 파일의 마지막 접근 날짜 
# atime =os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y년:%m월:%d일 %H:%M:%S"))


# # 파일 크기 
# size = os.path.getsize(file_path)
# print(size)


# 파일 목록 가져오기 
#print(os.listdir())  #모든 폴더 ,파일 목록 가져오기 
#print(os.listdir("1_excel"))
# print(os.listdir("2_desktop"))

# # 파일 목록 가져오기 (하위 폴더 모두 포함 )
#result = os.walk(".") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기 
# print(result)

# for root,dirs,files in result:
#     print(root,dirs,files)

# 만약 폴더 내에서 특정 파일들을 찾으려면? 

# name ="11_file_system.py"
# result = []
# for root, dirs,files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx , * txt , 자동화 *.png 를 찾으려면? 
# import fnmatch 
# pattern = "*.py" # .py 로 끝나는 모든 파일
# result=[]
# for root, dirs,files in os.walk("."):
#     for name in files:
#         #이름이 패턴과 일치하면
#         if fnmatch.fnmatch(name,pattern):
#             result.append(os.path.join(root,name))

# print(result)

# 주어진 경로가 파일이지? 폴더인지? 
# 폴더?
# print(os.path.isdir("1_excel"))
# # 파일?
# print(os.path.isfile("1_env.py"))

# print(os.path.isdir("checkBox.png"))
# print(os.path.isfile("checkBox.png"))

# 만약에 지정된 경로가 파일 /폴더가 없다면 ? 
# print(os.path.isdir("checkBox.png"))

#주어진 경로가 존재하는지?
# if os.path.exists("checkBox.png"):
#     print("파일또는 폴더가 존재합니다 ")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기 
#open("new_file.txt","a").close() # 빈 파일 생성 

# 파일명 변경하기
#os.rename("new_file.txt","new_file_rename.txt") 

# 파일 삭제하기 
#os.remove("new_file_rename.txt")

# 폴더 만들기
#os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성 
# os.mkdir("c:/....") # 절대 경로 기준으로 폴더 생성 

# os.mkdir("new_folder/a/b/c") #실패 : 하위 폴더를 가지는 폴더 생성 시도 
#os.makedirs("new_folder/a/b/c") # 성공 :하위 폴더를 가지는 폴더 생성 

# 폴더명 변경하기
#os.rename("new_folder","new_folder_rename")

# 폴더 지우기 
#os.rmdir("new_folder_rename") # 폴더 안이 비었을때만 삭제가능 

import shutil # shell utillities 줄임말
# shutil.rmtree("new_folder_rename") #폴더 안이 비어 있지 않아도 완전 삭제 가능 
 # 모든 파일이 삭제 될 수 있으므로 주의


# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기 

#shutil.copy("file_menu_notepad.png","test_folder") # 원본 경로 ,대상 경로
#shutil.copy("CheckBox.png","test_folder/copied_checkbox.png")#원본경로 ,대상경로

# 원본 파일 그대로 
# shutil.copy2("checkBox.png","2_desktop/test_folder/check2.png")
# # 현재 시간 그대로 
# shutil.copy("checkBox.png","2_desktop/test_folder/check.png")

#shutil.copytree("2_desktop/test_folder","2_desktop/test_folder2") # 원본 폴더 경로 ,대상 폴더 경로 

# 폴더 이동 
#shutil.move("2_desktop/test_folder","2_desktop/test_folder2")
#폴더명 변경되는 효과 
#shutil.move("2_desktop/test_folder2","2_desktop/test_folder")