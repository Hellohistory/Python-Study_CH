import time
import os

# 导入 Bindoer（Binod 爱好者）
print("您好，大家好！")
time.sleep(1)
print("让我们来找找 Binod！")


def checkBinod(file):
    """
    检查给定的文本文件是否包含“binod”单词。
    如果找到，则输出文件名和单词位置。
    如果没有找到，则返回 False。
    """
    with open(file, "r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        print(f"************** 恭喜找到 Binod ！在文件 {f} 中发现了！********************")
        return True
    else:
        return False


if __name__ == "__main__":
    print("************ Binod 检测器 ********************")
    dir_contents = os.listdir()
    for item in dir_contents:
        if item.endswith("txt"):
            ans = checkBinod(item)
            if ans is False:
                print("未找到 Binod，请尝试在其他地方寻找！")
