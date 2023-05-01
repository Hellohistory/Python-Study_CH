# 导入必要的模块
import qrcode

# 二维码生成器
query = input("输入内容:")  # 输入内容
code = qrcode.make(str(query))  # 生成二维码
code.save(input('请输入二维码名字:')+".png")  # 保存二维码文件
