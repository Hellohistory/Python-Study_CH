# 程序的主要功能是将12小时制转换为24小时制

from __future__ import print_function


def convert_time(input_str):
    # 验证输入时间格式是否正确
    if not validate_time(input_str):
        return "输入的时间格式不正确，请按照HH:MM:SS AM/PM格式输入"

    # 提取小时、分钟、秒和AM/PM信息
    time_components = input_str.split()
    time = time_components[0]
    am_pm = time_components[1]

    # 将字符串转换为24小时制
    if am_pm == "AM":
        if time == "12:00:00":
            return "00:00:00"
        else:
            return time
    else:  # PM
        if time == "12:00:00":
            return "12:00:00"
        else:
            hour, minute, second = map(int, time.split(':'))
            return '{:02d}:{:02d}:{:02d}'.format(hour + 12, minute, second)


def validate_time(input_str):
    # 验证时间格式是否为HH:MM:SS AM/PM
    if len(input_str) != 11:
        return False

    time_components = input_str.split()
    time = time_components[0]
    am_pm = time_components[1]

    if am_pm not in ["AM", "PM"]:
        return False

    hour, minute, second = time.split(':')
    if not (0 <= int(hour) <= 12):
        return False
    if not (0 <= int(minute) < 60):
        return False
    if not (0 <= int(second) < 60):
        return False

    return True


if __name__ == "__main__":
    input_time = input("输入您要转换的时间：")
    print(convert_time(input_time))
