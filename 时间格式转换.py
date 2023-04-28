from __future__ import print_function

# Created by sarathkaul on 12/11/19


def convert_time(input_str):
    # 检查时间的最后两个元素是否为AM，前两个元素是否为12
    if input_str[-2:] == "AM" and input_str[:2] == "12":
        return "00" + input_str[2:-2]

    # 去掉AM
    elif input_str[-2:] == "AM":
        return input_str[:-2]

    # 检查时间的最后两个元素是否为PM，前两个元素是否为12
    elif input_str[-2:] == "PM" and input_str[:2] == "12":
        return input_str[:-2]

    else:
        # 将小时加12并去掉PM
        return str(int(input_str[:2]) + 12) + input_str[2:8]


if __name__ == "__main__":
    input_time = input("输入您要转换的时间:")
    print(convert_time(input_time))