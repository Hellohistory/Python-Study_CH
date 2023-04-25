"""
这段代码是一个密码验证程序，用户需要输入一个密码，然后通过输入多次可能正确的密码来验证是否记得原始密码。
如果在前5次尝试中没有成功，程序将暂停30秒钟，然后再次尝试。如果记住密码，则输出“正确的密码”，否则输出“不正确的密码”。
"""
import time

pwd=input("请输入您的密码： ")    #设置您的密码

def IInd_func():
  count1=0
  for j in range(5):
    a=0
    count=0
    user_pwd = input("请输入您记得的密码： ")        #您记得的密码
    for i in range(len(pwd)):
      if user_pwd[i] == pwd[a]:       #将记得的密码与固定密码进行比较
        a +=1
        count+=1
    if count==len(pwd):
      print("密码正确")
      break
    else:
      count1 += 1
      print("密码不正确")
  if count1==5:
    time.sleep(30)
    IInd_func()

IInd_func()