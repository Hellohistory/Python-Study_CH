num = int(input("请输入一个数字:"))  # 获取用户输入的数字
if (num % 2) == 0:  # 如果数字除以2的余数为0，则它是偶数
   print("{0} 是偶数".format(num))
else:  # 否则为奇数
   print("{0} 是奇数".format(num))
