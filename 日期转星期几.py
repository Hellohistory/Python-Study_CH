import re
import datetime
import calendar

# 定义正则表达式匹配不同日期格式
pattern = re.compile(r'(\d{4})[-/ ](\d{1,2})[-/ ](\d{1,2})')

# 定义星期几的中英文对应关系
weekday_dict = {
    "Monday": "星期一",
    "Tuesday": "星期二",
    "Wednesday": "星期三",
    "Thursday": "星期四",
    "Friday": "星期五",
    "Saturday": "星期六",
    "Sunday": "星期日"
}

# 获取用户输入的日期
input_date = input("请输入日期:")

# 使用正则表达式匹配输入日期
match = pattern.match(input_date)

if match:
    year, month, day = match.groups()
else:
    print("日期格式不正确！")
    exit()

# 将年月日转换为整型
year = int(year)
month = int(month)
day = int(day)

# 使用calendar模块判断输入日期是星期几
weekday = calendar.day_name[datetime.date(year, month, day).weekday()]
weekday_cn = weekday_dict[weekday]

# 输出结果
print("输入日期是：{}年{}月{}日，是{}".format(year, month, day, weekday_cn))
