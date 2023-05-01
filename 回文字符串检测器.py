# 定义一个字符串 my_str
my_str = 'aIbohPhoBiA'

# 将字符串转换为小写，以便进行大小写不敏感的比较
my_str = my_str.casefold()

# 反转字符串
rev_str = reversed(my_str)

# 检查反转后的字符串是否与原字符串相等
if list(my_str) == list(rev_str):
   print("该字符串是一个回文字符串。")
else:
   print("该字符串不是一个回文字符串。")